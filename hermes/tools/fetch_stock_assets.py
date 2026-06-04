"""
fetch_stock_assets.py — Hermès skill : récupération assets stock via Pexels API

Skill secondaire : récupère images/vidéos stock pour B-roll quand AI génération coûte trop ou prend trop de temps.

Pexels = gratuit + commercial use OK. Bon pour C2 (ambient B-roll) et C3 (screen recording fallback).
"""

import os
import sys
import requests
from pathlib import Path
from typing import List, Optional, Literal


PEXELS_API_BASE = "https://api.pexels.com/v1"
PEXELS_VIDEO_BASE = "https://api.pexels.com/videos"


def fetch_stock_assets(
    keywords: List[str],
    count: int = 5,
    asset_type: Literal["photo", "video"] = "photo",
    orientation: Literal["landscape", "portrait", "square"] = "landscape",
    min_resolution: Optional[int] = 1920,
    output_dir: Optional[Path] = None,
) -> List[Path]:
    """
    Récupère des assets stock via Pexels API.

    Args:
        keywords: liste de mots-clés (combinés en query).
        count: nombre d'assets à télécharger.
        asset_type: "photo" ou "video".
        orientation: "landscape" (16:9) / "portrait" (9:16 pour C4) / "square" (1:1).
        min_resolution: largeur minimum en pixels (défaut 1920 = HD min).
        output_dir: dossier output. Défaut = /tmp/stock-assets/.

    Returns:
        Liste des paths téléchargés.

    Raises:
        RuntimeError: si PEXELS_API_KEY non set OR API échoue.
    """
    api_key = os.getenv("PEXELS_API_KEY")
    if not api_key:
        raise RuntimeError(
            "PEXELS_API_KEY not set. Get free key: https://www.pexels.com/api/"
        )

    if output_dir is None:
        output_dir = Path("/tmp/stock-assets")
    output_dir.mkdir(parents=True, exist_ok=True)

    query = " ".join(keywords)

    # ===== Search =====
    if asset_type == "photo":
        url = f"{PEXELS_API_BASE}/search"
        params = {
            "query": query,
            "per_page": count * 2,  # over-fetch pour filtrer après
            "orientation": orientation,
        }
    else:  # video
        url = f"{PEXELS_VIDEO_BASE}/search"
        params = {
            "query": query,
            "per_page": count * 2,
            "orientation": orientation,
            "min_duration": 3,
            "max_duration": 30,
        }

    headers = {"Authorization": api_key}

    try:
        resp = requests.get(url, params=params, headers=headers, timeout=15)
        resp.raise_for_status()
    except requests.RequestException as e:
        raise RuntimeError(f"Pexels API error: {e}")

    data = resp.json()
    items = data.get("photos" if asset_type == "photo" else "videos", [])

    # ===== Filter + download =====
    downloaded: List[Path] = []

    for item in items:
        if len(downloaded) >= count:
            break

        # Pick best resolution
        if asset_type == "photo":
            src_url = item["src"]["original"]
            width = item.get("width", 0)
            if min_resolution and width < min_resolution:
                continue
            ext = ".jpg"
            asset_id = item["id"]
        else:  # video
            # Pexels video : pick smallest file >= min_resolution
            files = item.get("video_files", [])
            files_sorted = sorted(
                [f for f in files if f.get("width", 0) >= (min_resolution or 0)],
                key=lambda f: f.get("file_size", float("inf"))
            )
            if not files_sorted:
                continue
            src_url = files_sorted[0]["link"]
            ext = ".mp4"
            asset_id = item["id"]

        # Download
        try:
            r = requests.get(src_url, stream=True, timeout=60)
            r.raise_for_status()
        except requests.RequestException as e:
            print(f"⚠ Skip {asset_id}: {e}", file=sys.stderr)
            continue

        output_path = output_dir / f"pexels-{asset_id}{ext}"
        with open(output_path, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)

        downloaded.append(output_path)
        print(f"✓ Downloaded {output_path.name}", file=sys.stderr)

    if len(downloaded) < count:
        print(
            f"⚠ Only got {len(downloaded)}/{count} assets matching criteria. "
            f"Try broader keywords or relax min_resolution.",
            file=sys.stderr,
        )

    return downloaded


# ===== CLI usage =====
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Fetch stock assets from Pexels")
    parser.add_argument("--keywords", nargs="+", required=True)
    parser.add_argument("--count", type=int, default=5)
    parser.add_argument("--type", choices=["photo", "video"], default="photo")
    parser.add_argument("--orientation", choices=["landscape", "portrait", "square"], default="landscape")
    parser.add_argument("--min-resolution", type=int, default=1920)
    parser.add_argument("--output-dir", type=Path, default=None)

    args = parser.parse_args()

    paths = fetch_stock_assets(
        keywords=args.keywords,
        count=args.count,
        asset_type=args.type,
        orientation=args.orientation,
        min_resolution=args.min_resolution,
        output_dir=args.output_dir,
    )

    for p in paths:
        print(p)
