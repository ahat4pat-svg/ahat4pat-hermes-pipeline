"""
render_scene.py — Hermès skill : génération scène vidéo via Higgs Field / Modal / etc.

Skill principal pour la génération de clips IA selon SceneDefinition JSON schema.
Backend = Higgs Field (Seedance 2.0) recommandé pour qualité, OR Modal (Seedance 1.5) pour budget.
"""

import os
import sys
import json
import time
import requests
from pathlib import Path
from typing import Optional, Dict, Any


HIGGS_FIELD_API_BASE = "https://api.higgsfield.ai/v1"


def render_scene(
    data: Dict[str, Any],
    backend: str = "higgs_field",
    output_path: Optional[Path] = None,
    max_wait_seconds: int = 300,
) -> Path:
    """
    Génère un clip vidéo à partir d'une SceneDefinition.

    SceneDefinition schema attendue :
    {
      "scene_id": "001_chichen_itza",
      "visual_prompt": "Cinematic aerial view of Chichen Itza, 8k, golden hour",
      "reference_image": "path/to/ref.jpg" (optional),
      "duration_seconds": 5,
      "aspect_ratio": "16:9" | "9:16" | "1:1",
      "model": "seedance-2.0" | "seedance-1.5-pro" | "ltx-2",
      "temporal_weight": 0.85,
      "audio_enabled": true (default false),
      "negative_prompt": "blurry, low quality" (optional),
      "seed": 12345 (optional, pour reproductibilité)
    }

    Args:
        data: SceneDefinition dict.
        backend: "higgs_field" (paid premium) OR "modal_byteplus" (free Seedance 1.5).
        output_path: chemin output MP4.
        max_wait_seconds: timeout pour génération (Seedance peut prendre 60-180s).

    Returns:
        Path vers le MP4 généré.

    Raises:
        ValueError: si data invalide.
        RuntimeError: si API échoue.
    """
    # ===== Validation schema =====
    required = ["scene_id", "visual_prompt"]
    for field in required:
        if field not in data:
            raise ValueError(f"SceneDefinition missing required field: {field}")

    scene_id = data["scene_id"]
    visual_prompt = data["visual_prompt"]
    duration = data.get("duration_seconds", 5)
    aspect = data.get("aspect_ratio", "16:9")
    model = data.get("model", "seedance-2.0")
    temporal_weight = data.get("temporal_weight", 0.85)
    audio_enabled = data.get("audio_enabled", False)
    negative_prompt = data.get("negative_prompt", "blurry, low quality, distorted, slop, watermark")
    seed = data.get("seed")
    reference_image = data.get("reference_image")

    if not 0.0 <= temporal_weight <= 1.0:
        raise ValueError(f"temporal_weight {temporal_weight} doit être 0.0-1.0")

    # ===== Output path =====
    if output_path is None:
        output_dir = Path("/tmp/scenes")
        output_dir.mkdir(parents=True, exist_ok=True)
        output_path = output_dir / f"{scene_id}.mp4"
    else:
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)

    # ===== Backend dispatch =====
    if backend == "higgs_field":
        return _render_via_higgs_field(
            scene_id=scene_id,
            prompt=visual_prompt,
            duration=duration,
            aspect=aspect,
            model=model,
            negative_prompt=negative_prompt,
            seed=seed,
            reference_image=reference_image,
            audio_enabled=audio_enabled,
            output_path=output_path,
            max_wait=max_wait_seconds,
        )
    elif backend == "modal_byteplus":
        return _render_via_modal(
            scene_id=scene_id,
            prompt=visual_prompt,
            duration=duration,
            aspect=aspect,
            output_path=output_path,
            max_wait=max_wait_seconds,
        )
    else:
        raise ValueError(f"Unknown backend: {backend}")


def _render_via_higgs_field(
    scene_id: str,
    prompt: str,
    duration: int,
    aspect: str,
    model: str,
    negative_prompt: str,
    seed: Optional[int],
    reference_image: Optional[str],
    audio_enabled: bool,
    output_path: Path,
    max_wait: int,
) -> Path:
    api_key = os.getenv("HIGGS_FIELD_API_KEY")
    if not api_key:
        raise RuntimeError(
            "HIGGS_FIELD_API_KEY not set. Sign up: https://higgsfield.ai/"
        )

    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}

    # Submit job
    payload = {
        "model": model,
        "prompt": prompt,
        "duration": duration,
        "aspect_ratio": aspect,
        "negative_prompt": negative_prompt,
        "audio": audio_enabled,
    }
    if seed:
        payload["seed"] = seed
    if reference_image:
        # Higgs Field accepts image as URL or base64
        payload["reference_image_url"] = reference_image

    try:
        submit_resp = requests.post(
            f"{HIGGS_FIELD_API_BASE}/video/generate",
            json=payload,
            headers=headers,
            timeout=30,
        )
        submit_resp.raise_for_status()
    except requests.RequestException as e:
        raise RuntimeError(f"Higgs Field submit failed: {e}")

    job_id = submit_resp.json().get("job_id")
    if not job_id:
        raise RuntimeError(f"Higgs Field no job_id in response: {submit_resp.text}")

    # Poll until done
    start = time.time()
    while time.time() - start < max_wait:
        time.sleep(5)
        try:
            status_resp = requests.get(
                f"{HIGGS_FIELD_API_BASE}/video/status/{job_id}",
                headers=headers,
                timeout=15,
            )
            status_resp.raise_for_status()
        except requests.RequestException as e:
            print(f"⚠ Status check failed (will retry): {e}", file=sys.stderr)
            continue

        status_data = status_resp.json()
        status = status_data.get("status")

        if status == "completed":
            download_url = status_data.get("output_url")
            break
        elif status == "failed":
            raise RuntimeError(f"Higgs Field render failed: {status_data.get('error')}")
        # else: still processing, continue polling
    else:
        raise RuntimeError(f"Higgs Field render timeout after {max_wait}s")

    # Download
    try:
        r = requests.get(download_url, stream=True, timeout=120)
        r.raise_for_status()
    except requests.RequestException as e:
        raise RuntimeError(f"Higgs Field download failed: {e}")

    with open(output_path, "wb") as f:
        for chunk in r.iter_content(chunk_size=8192):
            f.write(chunk)

    print(f"✓ Scene rendered: {output_path}", file=sys.stderr)
    return output_path


def _render_via_modal(
    scene_id: str,
    prompt: str,
    duration: int,
    aspect: str,
    output_path: Path,
    max_wait: int,
) -> Path:
    """
    Backend Modal + Byte Plus Seedance 1.5 Pro (free credits).
    À implémenter quand Modal endpoint déployé.
    """
    raise NotImplementedError(
        "Modal+ByteBlus backend pas encore implémenté. "
        "Utilise 'higgs_field' OR implémente endpoint dans docker/modal-seedance/app.py"
    )


# ===== CLI usage =====
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Render scene via Higgs Field or Modal")
    parser.add_argument("--data", required=True, help="Path to SceneDefinition JSON file")
    parser.add_argument("--backend", default="higgs_field", choices=["higgs_field", "modal_byteplus"])
    parser.add_argument("--output", default=None, type=Path)

    args = parser.parse_args()

    with open(args.data) as f:
        scene_data = json.load(f)

    path = render_scene(
        data=scene_data,
        backend=args.backend,
        output_path=args.output,
    )
    print(path)
