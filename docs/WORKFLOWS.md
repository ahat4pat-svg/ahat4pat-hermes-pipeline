# WORKFLOWS

## 5 workflows par TL/channel (mappés sur NotebookLM docs)

| Workflow | TL / Channel | Voir |
|----------|--------------|------|
| Storytelling Visuel | TL Faceless YT C1 Stillcraft | `workflows/c1-storytelling.md` (TODO) |
| Documentaires Longs Swarm | TL Faceless YT C2 Loopkeeper | `workflows/c2-documentaires.md` (TODO) |
| Tutorial Drew-style FR-CA | TL Faceless YT C3 Stacklab | [`workflows/c3-tutorials.md`](workflows/c3-tutorials.md) ✅ |
| News-Jacker shorts | TL Faceless YT C4 Karmawatch | [`workflows/c4-newsjacker.md`](workflows/c4-newsjacker.md) ✅ |
| Anti-Gravity B2B | TL Juniors4Pat | TODO |

## Stack technique commun

```
Brief MD (Claude) → Script (Claude) → Voice (ElevenLabs/MiniMax) → Visuals (FLUX/LTX-2/Seedance) → Stitch (ffmpeg) → Upload (YouTube API)
```

Orchestration : n8n trigger → Claude Code CLI → Hermès delegation → TL sub-agent → tools.

## Règles transversales (4 règles Romayroh + Burney)

1. Long-form 10-20 min
2. Chapters dans description
3. Description 500+ mots avec entités nommées
4. Transcript manuel uploadé (PAS auto-caption)
5. Burney style sous-titres karaoké (mot actif accent couleur)

## Voice règles

- Speaking rate 0.9-1.2 strict
- JAMAIS default voices ElevenLabs
- Voix Pat réelle > clone pat_custom > MiniMax > Google AI Studio TTS
