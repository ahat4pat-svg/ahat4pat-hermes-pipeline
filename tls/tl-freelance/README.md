# TL Freelance

> Team Leader · Freelance pipeline (Team A IMAP scout + Team B PME outreach)
> Reports to : Claude (Director)
> Audité par : Patou-Overseer (independent)

## Mission

Génération de leads + envoi de propositions pour Pat, dans 2 streams parallèles :

- **Team A (IMAP)** : scout les courriels entrants (Upwork notifications + outreach directs) et drafte des réponses adaptées
- **Team B (PME QC)** : génère des propositions cold à destination de PMEs québécoises (Mauricie d'abord, puis QC large)

## État actuel (2026-06-04)

- **Team A** : actif via Hermes IMAP scout. Patterns détectés : « Personal note from client » + 4 patterns outreach (`PERSONAL_OUTREACH_PATTERNS`)
- **Team B** : 62 drafts dormants dans `~/Linux/freelance/team-b-proposals.jsonl` — **attente review batch par Pat**
- **Email business** : `contact@ahat4pat.com`
- **Profile Upwork** : https://www.upwork.com/freelancers/~010124c5ea5855a6aa

## Sous-agents Hermès

| Sous-agent | Rôle | Modèle |
|------------|------|--------|
| `freelance-scout` | Scanne Inbox + Upwork notifications, classe par opportunité | DeepSeek V3.2 via OR |
| `freelance-drafter` | Drafte propositions personnalisées (FR-CA + EN) | DeepSeek V3.2 via OR |
| `freelance-follow-up` | Relance après 7 jours sans réponse | DeepSeek V3.2 (cooldown 24h, pas spam) |
| `freelance-pme-cold` | Génère cold proposals PME QC | DeepSeek V3.2 via OR |

## Fichiers et état

| Path | Description |
|------|-------------|
| `~/Linux/freelance/team-b-proposals.jsonl` | 62 drafts en attente review Pat |
| `~/Linux/freelance/lettres-pretes/` | 17 lettres dispute (Visa) + lettres cold prêtes |
| `~/Linux/ops-control/data/email-leads.jsonl` | Leads détectés par Team A IMAP |
| `~/Linux/ops-control/data/email-followup-seen.json` | Suivi cooldown 24h relances |
| `~/.hermes/state/visa-followup-state.json` | État relances Visa (séparé du freelance) |

## Blockers

- Pat doit reviewer les 62 drafts Team B PME (batch processing)
- AI Agents Sales (Pat enverra 4 vidéos pour digestion) — repositionne Team B vers ce vertical

## Prochaine milestone

- Pat batch-review 5-10 drafts cette semaine et envoie les premiers approuvés
- AI Agents Sales vidéos digérées + integration dans pitches Team B

## Liens

- [ORG_CHART du repo principal](../../ORG_CHART.md)
- [memory.md](memory.md)
- [project.json](project.json)
