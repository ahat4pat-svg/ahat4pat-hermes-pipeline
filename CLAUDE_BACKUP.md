# Claude Backup — Failover spec

> Pat 4 juin : « Tu n'as pas placé ton Claude Backup, qui est supposé être prêt depuis deux jours non plus. J'aimerais que tu le mettes là, puis que tu automatises le fait qu'il tombe automatiquement dessus avec toutes tes infos. Si ça chie, ça serait important. »

## ❓ Question pour Pat (avant config)

Je ne sais pas exactement quelle infra Pat a setup pour "Claude Backup" depuis 2 jours. **3 possibilités** :

1. **Claude Code instance sur Beck Hetzner** — j'ai vu dans CLAUDE.md que Beck a OpenCode 1.4.0 + Claude Code installés. Possible que c'est ça le backup.
2. **Claude via Nous Portal Plus** — déjà utilisé pour freelance-coo (subscription `ahat4pat@gmail.com`).
3. **LiteLLM fallback chain** — déjà en place : `ceo-think → ceo-fast`, `cto → ceo-fast`.

**Pat doit me dire lequel** OU me pointer où c'est setup.

## Spec failover (générique, applicable aux 3 options)

### Triggers de failover automatique

- Claude principal silent > 5 min en milieu de tâche critique
- Claude principal renvoie erreur API persistante (3 retries)
- Patou-Overseer détecte Claude divergent vs org chart > 3 fois en 24h

### Synchronisation (info que le backup doit avoir)

- ✅ Accès au repo `ahat4pat-hermes-pipeline` (clone local)
- ✅ Mémoire système (`~/.claude/projects/*/memory/`)
- ✅ CLAUDE.md règles
- ✅ RESUME-HERE-CLAUDE-[date].md sur Desktop
- ✅ Accès aux mêmes API keys (.env)
- ✅ Accès Telegram bot pour Pat (même chat_id)

### Mécanisme de bascule

```
1. Patou-Overseer détecte trigger
2. Patou envoie alerte Telegram à Pat : "Claude principal down — failover Backup active"
3. Patou démarre Claude Backup avec :
   - context = dernier RESUME-HERE + dernière conversation tronquée
   - identité = continuité de la conversation (pas un reset)
4. Pat reçoit message du Backup : "Salut Pat, je suis le backup. Je suis à jour. On continue où ?"
5. Pat valide ou rejette
```

### Setup à faire (1h)

- [ ] Pat confirme quelle infra = Claude Backup
- [ ] Setup cron : sync `~/.claude/projects/*/memory/` vers backup location toutes les heures
- [ ] Setup cron : sync `RESUME-HERE-*.md` toutes les 15 min
- [ ] Configure Patou-Overseer trigger (ajouter check `claude_principal_alive`)
- [ ] Test failover : simuler crash, vérifier backup reprend
- [ ] DRY_RUN 48h puis production

### Position dans org chart

```
   Claude (Director)  ←──   Claude Backup (standby, sync continu)
                              └ active si principal silent > 5 min
```

## Status

🟡 **Specs prêtes — manque info Pat sur quelle infra existante utiliser comme backup.**

Question directe Pat : « Le Claude Backup que tu as setup depuis 2 jours, c'est lequel des 3 (Beck / Nous Portal Plus / LiteLLM chain) ? »
