# hermes/

> Hermès Agent core config + tools.
> Framework : [NousResearch/hermes-agent](https://github.com/mz2/hermes-agent-sdk) (MIT, 140k GitHub stars).

## Structure

- `agent.py` — entry point scaffold (real implementation pending)
- `tools/` — typed Python skills :
  - `generate_voiceover.py` — ElevenLabs synthesis with speaking rate guards
  - `fetch_stock_assets.py` — Pexels API stock images/videos
  - `render_scene.py` — Higgs Field Seedance 2.0 OR Modal Byte Plus
  - `stitch_video.py` — ffmpeg assembly with `-shortest` flag

## Status

🟡 Scaffold only. Real implementation requires :
1. Clone Hermès SDK : `git clone https://github.com/mz2/hermes-agent-sdk.git`
2. Install : `pip install hermes-agent`
3. Configure `.env` (see root `.env.example`)
4. Implement skill registration patterns
5. Wire up to TLs in `tls/`

## Règles verrouillées

- **JAMAIS** default voices ElevenLabs (Adam, Bella, etc.)
- **Speaking rate 0.9-1.2** strict
- **Zero-padding** scene_001.mp4 obligatoire (ffmpeg concat)
- **Flag `-shortest`** impératif ffmpeg
- **Skills auto-generated** : Hermès écrit ses propres skills markdown après tâches complexes (différenciateur vs OpenClaw)
