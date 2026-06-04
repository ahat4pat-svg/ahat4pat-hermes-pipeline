"""
generate_voiceover.py — Hermès skill : synthèse vocale via ElevenLabs

Cette skill est invoquée par les TLs pour générer du voiceover.
Compatible avec n'importe quel TL qui a besoin de voix synthétique.

Voice clone Pat = voice_id `pat_custom` (à créer via UI ElevenLabs après record 30 sec).
Speaking rate 0.9-1.2 IMPÉRATIF (sinon rétention chute).
JAMAIS default voices (= AI slop detection par YT).
"""

import os
import sys
from pathlib import Path
from typing import Optional

try:
    from elevenlabs import ElevenLabs, VoiceSettings
except ImportError:
    print("Install: pip install elevenlabs", file=sys.stderr)
    sys.exit(1)


# ===== Config =====
FORBIDDEN_VOICES = ["Adam", "Bella", "Antoni", "Rachel", "Sarah", "Domi", "Elli"]
DEFAULT_MODEL_ID = os.getenv("ELEVENLABS_MODEL_ID", "eleven_multilingual_v2")
DEFAULT_SPEAKING_RATE = float(os.getenv("ELEVENLABS_SPEAKING_RATE", "1.1"))


def generate_voiceover(
    script: str,
    voice_id: Optional[str] = None,
    output_path: Optional[Path] = None,
    speaking_rate: float = DEFAULT_SPEAKING_RATE,
    model_id: str = DEFAULT_MODEL_ID,
    stability: float = 0.5,
    similarity_boost: float = 0.75,
) -> Path:
    """
    Génère un voiceover via ElevenLabs et sauvegarde en MP3.

    Args:
        script: texte à synthétiser. Peut contenir balises [whisper], [ton sec], etc.
        voice_id: ID voice ElevenLabs. Défaut = ELEVENLABS_VOICE_ID_PAT env var.
        output_path: chemin output MP3. Défaut = auto-generated dans /tmp/voiceovers/.
        speaking_rate: 0.9-1.2 (validé). Hors range = ValueError.
        model_id: défaut eleven_multilingual_v2 (FR-CA support).
        stability: 0.0-1.0 (0.5 = balanced).
        similarity_boost: 0.0-1.0 (0.75 = strong voice match).

    Returns:
        Path vers le MP3 généré.

    Raises:
        ValueError: si speaking_rate hors range OR voice_id est dans FORBIDDEN_VOICES.
        RuntimeError: si ELEVENLABS_API_KEY non set OR génération API échoue.
    """
    # ===== Guards =====
    if not 0.9 <= speaking_rate <= 1.2:
        raise ValueError(
            f"speaking_rate {speaking_rate} hors range 0.9-1.2 "
            f"(rétention chute hors range — règle verrouillée)"
        )

    api_key = os.getenv("ELEVENLABS_API_KEY")
    if not api_key:
        raise RuntimeError(
            "ELEVENLABS_API_KEY not set in env. "
            "Set in .env file or export ELEVENLABS_API_KEY=sk-..."
        )

    voice_id = voice_id or os.getenv("ELEVENLABS_VOICE_ID_PAT")
    if not voice_id:
        raise RuntimeError(
            "No voice_id provided AND ELEVENLABS_VOICE_ID_PAT not set. "
            "Create Pat voice clone via elevenlabs.io → Voice Lab → Instant Voice Cloning."
        )

    # Check against forbidden defaults (no AI slop on our channels)
    for forbidden in FORBIDDEN_VOICES:
        if forbidden.lower() in voice_id.lower():
            raise ValueError(
                f"voice_id '{voice_id}' matches forbidden default voice '{forbidden}'. "
                f"Use custom clone (pat_custom) or hire human voiceover."
            )

    # ===== Output path =====
    if output_path is None:
        output_dir = Path("/tmp/voiceovers")
        output_dir.mkdir(parents=True, exist_ok=True)
        # Auto-name based on script hash + timestamp
        import hashlib
        script_hash = hashlib.md5(script.encode()).hexdigest()[:8]
        output_path = output_dir / f"vo-{script_hash}.mp3"
    else:
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)

    # ===== Generate =====
    client = ElevenLabs(api_key=api_key)

    voice_settings = VoiceSettings(
        stability=stability,
        similarity_boost=similarity_boost,
        style=0.0,                    # neutral (use emotion tags inline)
        use_speaker_boost=True,
    )

    try:
        # Stream audio chunks
        audio_stream = client.text_to_speech.convert(
            text=script,
            voice_id=voice_id,
            model_id=model_id,
            voice_settings=voice_settings,
        )

        with open(output_path, "wb") as f:
            for chunk in audio_stream:
                f.write(chunk)

    except Exception as e:
        raise RuntimeError(f"ElevenLabs generation failed: {e}")

    print(f"✓ Voiceover generated: {output_path}", file=sys.stderr)
    return output_path


# ===== CLI usage =====
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Generate voiceover via ElevenLabs")
    parser.add_argument("--script", required=True, help="Text to synthesize OR path to .md file")
    parser.add_argument("--voice-id", default=None, help="ElevenLabs voice ID (default: pat_custom)")
    parser.add_argument("--output", default=None, help="Output MP3 path")
    parser.add_argument("--speaking-rate", type=float, default=DEFAULT_SPEAKING_RATE)

    args = parser.parse_args()

    # If script is a path, read it
    script_arg = args.script
    if Path(script_arg).is_file():
        script = Path(script_arg).read_text()
    else:
        script = script_arg

    path = generate_voiceover(
        script=script,
        voice_id=args.voice_id,
        output_path=Path(args.output) if args.output else None,
        speaking_rate=args.speaking_rate,
    )
    print(path)
