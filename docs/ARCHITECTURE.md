# ARCHITECTURE

Voir [ORG_CHART.md](../ORG_CHART.md) pour le schéma hiérarchique complet.

## Couche par couche

- **Pat** (CEO + Founder) — décisions stratégiques irréversibles, validation finale
- **Claude Code** (Director) — interlocuteur unique de Pat, orchestre, délègue
- **Patou-Overseer** (Watchdog) — surveille 7 sources direct, alerte Pat
- **Hermès Agent** (Executor) — heavy lift, sub-agents par TL
- **6 TLs** — un département chacun
- **Claude Backup** — failover si principal silent > 5 min

## Repos externes utilisés (pas clonés ici)

- Hermès Agent SDK : https://github.com/mz2/hermes-agent-sdk
- HyperFrames core : https://github.com/ReparoIN/hyperframes
- HyperFrames harness : https://github.com/xwxga/html-hyperframes-harness
- Claude Code skills 66 curated : https://github.com/hoanghd218/claude-code-2-days

## Install references

```bash
npm install remotion @remotion/cli
npm install -g @anthropic-ai/claude-code
pip install elevenlabs requests
```
