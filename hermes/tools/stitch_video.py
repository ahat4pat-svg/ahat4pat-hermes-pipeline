"""
stitch_video.py — Hermès skill : assemblage final via ffmpeg

Skill critique : transforme audio + clips vidéo en MP4 final.

Règles verrouillées :
- Flag `-shortest` IMPÉRATIF (anti silence gênant)
- Zero-padding scene_001.mp4 obligatoire (anti sort alpha bug ffmpeg)
- Format output : MP4 H.264 (compatible YouTube tous devices)
"""

import os
import sys
import subprocess
from pathlib import Path
from typing import List, Optional


def stitch_video(
    audio: Path,
    clips: List[Path],
    output_path: Path,
    aspect_ratio: str = "16:9",
    add_background_music: Optional[Path] = None,
    music_volume_db: float = -20.0,
) -> Path:
    """
    Assemble audio voiceover + clips vidéo en MP4 final.

    Args:
        audio: path vers le voiceover principal (WAV ou MP3).
        clips: liste paths vers les clips vidéo, dans l'ordre. Zero-padding requis.
        output_path: path output MP4.
        aspect_ratio: "16:9" (horizontal) ou "9:16" (vertical C4).
        add_background_music: optionnel, path vers musique de fond.
        music_volume_db: niveau musique fond (défaut -20dB = subtil).

    Returns:
        Path vers le MP4 final.

    Raises:
        ValueError: si zero-padding violé OR clips vides OR audio inexistant.
        RuntimeError: si ffmpeg échoue.
    """
    # ===== Guards =====
    if not audio.is_file():
        raise ValueError(f"Audio file missing: {audio}")

    if not clips:
        raise ValueError("clips list cannot be empty")

    for c in clips:
        if not c.is_file():
            raise ValueError(f"Clip missing: {c}")
        # Check zero-padding (scene_001.mp4 not scene_1.mp4)
        name = c.stem
        if "_" in name:
            num_part = name.split("_")[-1]
            if num_part.isdigit() and len(num_part) < 3:
                raise ValueError(
                    f"Clip {c.name} viole zero-padding (doit être scene_001.mp4 pas scene_1.mp4). "
                    f"Sinon ffmpeg concat dans le mauvais ordre alphabétique."
                )

    output_path.parent.mkdir(parents=True, exist_ok=True)

    # ===== Stage 1 : concat clips en 1 vidéo intermédiaire =====
    concat_list_path = Path(f"/tmp/ffmpeg-concat-{os.getpid()}.txt")
    with open(concat_list_path, "w") as f:
        for c in clips:
            f.write(f"file '{c.absolute()}'\n")

    intermediate_video = Path(f"/tmp/concat-{os.getpid()}.mp4")

    concat_cmd = [
        "ffmpeg", "-y",
        "-f", "concat",
        "-safe", "0",
        "-i", str(concat_list_path),
        "-c", "copy",
        str(intermediate_video),
    ]

    try:
        result = subprocess.run(concat_cmd, capture_output=True, text=True, check=True)
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"ffmpeg concat failed: {e.stderr}")

    # ===== Stage 2 : mux audio + (optional music) =====
    final_cmd = ["ffmpeg", "-y", "-i", str(intermediate_video), "-i", str(audio)]

    if add_background_music and add_background_music.is_file():
        # 3 inputs : video + voice + music
        final_cmd.extend(["-i", str(add_background_music)])
        # filter : mix voice + music (lower music)
        filter_complex = (
            f"[2:a]volume={music_volume_db}dB[music];"
            f"[1:a][music]amix=inputs=2:duration=shortest[aout]"
        )
        final_cmd.extend([
            "-filter_complex", filter_complex,
            "-map", "0:v",
            "-map", "[aout]",
        ])
    else:
        # 2 inputs : video + voice only
        final_cmd.extend(["-map", "0:v", "-map", "1:a"])

    # Critical : -shortest flag (CAR LA VIE) + H.264 + AAC audio
    final_cmd.extend([
        "-c:v", "libx264",
        "-preset", "medium",
        "-crf", "23",
        "-c:a", "aac",
        "-b:a", "192k",
        "-shortest",                  # IMPÉRATIF — anti silence gênant
        "-movflags", "+faststart",    # YouTube streaming optimal
        str(output_path),
    ])

    try:
        result = subprocess.run(final_cmd, capture_output=True, text=True, check=True)
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"ffmpeg final stitch failed: {e.stderr}")

    # Cleanup intermediate
    concat_list_path.unlink(missing_ok=True)
    intermediate_video.unlink(missing_ok=True)

    print(f"✓ Video stitched: {output_path}", file=sys.stderr)
    return output_path


# ===== CLI usage =====
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Stitch audio + clips into final MP4 via ffmpeg")
    parser.add_argument("--audio", required=True, type=Path)
    parser.add_argument("--clips", nargs="+", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--aspect", default="16:9", choices=["16:9", "9:16"])
    parser.add_argument("--music", default=None, type=Path)

    args = parser.parse_args()

    path = stitch_video(
        audio=args.audio,
        clips=args.clips,
        output_path=args.output,
        aspect_ratio=args.aspect,
        add_background_music=args.music,
    )
    print(path)
