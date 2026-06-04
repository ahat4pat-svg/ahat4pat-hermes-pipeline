# ahat4pat-hermes-pipeline

> Multi-channel faceless YouTube + B2B AI agents pipeline.
> Hermès Agent (NousResearch) as executor · Claude Code as director · Patou-Overseer as watchdog.
> 6 Team Leaders · 4 YouTube channels · full automation.

## Org chart

```
                    Pat (CEO + Founder)
                          │
            ┌─────────────┴─────────────┐
            │                            │
   Claude (Director)            Patou-Overseer (Watchdog)
   = orchestration              = accountability INDÉPENDANTE
            │                            │
   ┌────────┼────────┐                   │
   │        │        │                   │
   TLs (6 départements) ◄─ surveillés DIRECT par Patou
   │
   ├─ TL Faceless YT  (4 channels : Stillcraft / Loopkeeper / Stacklab / Karmawatch)
   ├─ TL Juniors4Pat  (AI Agents Sales B2B)
   ├─ TL Freelance    (Team A IMAP + Team B PME)
   ├─ TL Voice Services International
   ├─ TL KDP / Newsletter / Écriture
   └─ TL Musique      (Pat + Ju, perso)
```

## Stack

- **Hermès Agent** (NousResearch, 140k GitHub stars, MIT) — executor
- **Claude Code CLI** — director interface
- **n8n** — orchestrateur production (déjà en place)
- **Modal GPU** — compute serverless ($30/mo Starter free credit)
- **Cloudflare R2** — storage (10GB free, zero egress)
- **ElevenLabs** ou **Qwen3-TTS** — voice
- **FLUX.2 / LTX-2 / Seedance** — image-to-video
- **HyperFrames** ou **Remotion** — composition
- **ffmpeg** — assemblage final

## Workflows par TL

| TL | Workflow source | Spec doc |
|----|-----------------|----------|
| TL Faceless YT C1 Stillcraft | Storytelling Visuel | docs/workflows/c1-storytelling.md |
| TL Faceless YT C2 Loopkeeper | Documentaires Longs (Swarm 3 agents) | docs/workflows/c2-documentaires.md |
| TL Faceless YT C3 Stacklab | Tutorial Educational Drew-style FR-CA | docs/workflows/c3-tutorials.md |
| TL Faceless YT C4 Karmawatch | News-Jacker shorts 1080×1920 | docs/workflows/c4-newsjacker.md |
| TL Juniors4Pat | Anti-Gravity Direct-to-Client B2B | docs/workflows/j4p-b2b.md |
| TL Freelance / Voice / KDP / Musique | À définir per TL | docs/workflows/*.md |

## Structure

```
ahat4pat-hermes-pipeline/
├── README.md                      ← ce fichier
├── ORG_CHART.md                   ← détail des responsabilités par couche
├── memory.md                      ← lexicon global + verrouillage architectural
├── project.json                   ← master state file
├── .env.example                   ← template variables d'environnement
│
├── tls/                           ← 6 team leaders (1 dossier chacun)
├── hermes/                        ← Hermès Agent core config + tools
├── overseer/                      ← Patou-Overseer Python wrapper
├── pipeline/                      ← Docker + n8n workflows production
├── briefs/                        ← briefs de production par vidéo
└── docs/                          ← architecture, workflows, références
```

## Setup

1. Clone ce repo
2. `cp .env.example .env` puis remplir les keys
3. `npm install -g @anthropic-ai/claude-code`
4. Cloner les frameworks externes :
   ```bash
   git clone https://github.com/mz2/hermes-agent-sdk.git external/hermes-agent-sdk
   git clone https://github.com/ReparoIN/hyperframes.git external/hyperframes
   git clone https://github.com/xwxga/html-hyperframes-harness.git external/hyperframes-harness
   ```
5. Configurer Modal : `modal setup`
6. Tester pipeline avec `cd briefs && claude '/video c3-stacklab/01-n8n-claude-lead-scoring-bot.md'`

## Accountability

Patou-Overseer scan **7 sources** (Claude director + 6 TLs) 2× par jour (9h + 20h). Alerte Telegram à Pat directement si dérive. Configuration : `overseer/targets.json`.

`DRY_RUN=1` par défaut. Mettre `0` quand validé 48h.

## Repos externes utilisés

- [Hermès Agent SDK](https://github.com/mz2/hermes-agent-sdk) — orchestrateur
- [HyperFrames](https://github.com/ReparoIN/hyperframes) — composition vidéo programmatique
- [HyperFrames Harness](https://github.com/xwxga/html-hyperframes-harness) — Director Workbench
- [Claude Code 2 Days](https://github.com/hoanghd218/claude-code-2-days) — 66 skills curated
- [Remotion](https://github.com/remotion-dev/remotion) — React video framework

## License

MIT (suit la licence Hermès Agent)

## Status

🟡 **In progress** — Build initial 4 juin 2026. Première vidéo test C3 prévue ce soir.

## Contact

- CEO : Pat (ahat4pat@gmail.com)
- Director : Claude (via conversation)
- Watchdog : Patou-Overseer (cron 9h/20h, Telegram)
