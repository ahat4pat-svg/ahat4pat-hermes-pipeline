# overseer/

> Patou-Overseer = accountability indépendante.
> Surveille **7 sources** (Claude director + 6 TLs).
> Alerte Pat **DIRECTEMENT** via Telegram si dérive (pas via Claude).

## Principe

```
Patou surveille DIRECT :
- Claude (Director) → check org chart consistency
- TL Faceless YT → check no drift from briefs
- TL Juniors4Pat → check waitlist growth + SLA
- TL Freelance → check leads pipeline health
- TL Voice Services → check Twilio balance + voice inventory
- TL KDP / Newsletter → check publication cadence + Pat voice compliance
- TL Musique → check sessions logged (perso, checks minimaux)

Si dérive → Telegram à Pat (pas via Claude)
```

## Config

- `targets.json` — 7 sources + checks per target
- `DRY_RUN=1` par défaut (log only, no Telegram send)
- Cron schedule : `09:00 + 20:00`

## Status

🟡 Scaffold only. `patou_overseer.py` charge config, parse env, placeholder run loop.

## Activation production

1. Set env vars : `TELEGRAM_BOT_TOKEN_PATOU`, `TELEGRAM_CHAT_ID_PAT`
2. Validate 48h en `DRY_RUN=1` (vérifier logs `~/Documents/Patou-Vault/dry-run-YYYY-MM-DD.log`)
3. Si OK : `DRY_RUN=0` en production
4. Cron job : `0 9,20 * * * cd /path/to/repo && python overseer/patou_overseer.py`
