# pipeline/

> Production infrastructure : Docker + n8n workflows.

## Structure

- `docker/modal-qwen3-tts/` — Qwen3-TTS deployment on Modal GPU
- `docker/modal-flux/` — FLUX.2 image generation on Modal
- `docker/modal-ltx2/` — LTX-2 image-to-video on Modal
- `n8n-workflows/` — JSON workflows pour n8n local Pat
  - `ahat4pat-pipeline-trigger.json` — main cron trigger (9h daily)

## Modal setup

```bash
modal setup
modal deploy docker/modal-qwen3-tts/app.py
modal deploy docker/modal-flux/app.py
modal deploy docker/modal-ltx2/app.py
```

Free tier : $30/mo starter credit. Suffit pour plusieurs vidéos complexes.

## n8n import

1. Ouvrir n8n local : http://localhost:5678
2. Import → `n8n-workflows/ahat4pat-pipeline-trigger.json`
3. Configure credentials (S3 R2, YouTube OAuth)
4. Activate workflow

## Status

🟡 Scaffold seulement. Docker apps à implémenter quand Modal credits validés.
