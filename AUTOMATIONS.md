# Automations — Catalogue + état + priorités

> Préparé : 2026-06-04
> Vue d'ensemble des automations actives + planned + souhaitables pour AHat4Pat
> Priorisation par ROI temps Pat + Phase 1 cash impact

## Principe directeur

**Toute action que Pat fait plus d'1× par semaine = candidate pour automation.**

L'objectif n'est pas d'éliminer Pat — c'est d'éliminer les tâches mécaniques pour qu'il reste sur la décision, la stratégie, la créativité.

---

## Catalogue par TL

### TL Faceless YT (4 channels)

| Automation | État | Effort setup | ROI | Priorité |
|------------|------|-------------|-----|----------|
| Brief → script Claude | Scaffolded | 2h | Haut (par vidéo) | 🔥 P1 |
| Script → voice ElevenLabs | Tool prêt | 1h | Haut | 🔥 P1 |
| Fetch B-roll Pexels | Tool prêt | 1h | Moyen | 🔥 P1 |
| Render scenes Higgs Field | Tool prêt | 2h | Moyen | 🔥 P1 |
| Stitch ffmpeg | Tool prêt | 1h | Bas (un seul shot) | 🔥 P1 |
| Upload YouTube + chapters + transcript | Skill scaffold | 2h | Haut (par vidéo) | 🔥 P1 |
| Whisper transcription auto | À créer | 1h | Haut | 🔶 P2 |
| Burney karaoké subs auto | À créer | 3h | Haut (visuel) | 🔶 P2 |
| YouTube analytics → dashboard | À créer | 2h | Moyen | 🟢 P3 |
| Thumbnail auto-gen + A/B | À créer | 4h | Haut (CTR impact) | 🔶 P2 |

**Bloquage actuel** : API keys (ELEVENLABS + GOOGLE_AI + YOUTUBE + MODAL). Une fois fournies, P1 tout entier débloque.

### TL Juniors4Pat

| Automation | État | Effort setup | ROI | Priorité |
|------------|------|-------------|-----|----------|
| Stripe webhook → CRM | ✅ Actif | — | Critique | ✅ |
| Email confirmation order | ✅ Actif | — | Haut | ✅ |
| Junior4pat-webhook health check | ✅ Actif | — | Critique | ✅ |
| Tunnel Cloudflare auto-restart | ✅ Actif | — | Critique | ✅ |
| Order routing → bon agent / livrable | 🔶 Partial | 4h | Haut | 🔥 P1 |
| Customer success follow-up J+7 J+30 | À créer | 2h | Haut (retention) | 🔥 P1 |
| Upsell auto-detection (Starter usage > seuil) | À créer | 3h | Haut (revenue) | 🔶 P2 |
| Churn risk detection (usage drop) | À créer | 3h | Haut (retention) | 🔶 P2 |

### TL Freelance

| Automation | État | Effort setup | ROI | Priorité |
|------------|------|-------------|-----|----------|
| Team A IMAP scout (LEAD_FROID/CHAUD classify) | ✅ Actif | — | Haut | ✅ |
| Team B PME drafter (62 drafts dormants) | ✅ Actif | — | Haut | ✅ |
| Email follow-up cooldown 24h | ✅ Actif | — | Critique (anti-spam) | ✅ |
| Pattern « Personal note from client » detection | ✅ Actif | — | Haut | ✅ |
| Auto-draft response sur Upwork notifs (DRAFT only, Pat reviews) | À créer | 4h | Très haut (Pat lent à répondre) | 🔥 P1 |
| Score lead → priorité dans inbox Pat | À créer | 2h | Haut | 🔶 P2 |
| Auto-archive LinkedIn invitations cold (~80% noise) | À créer | 1h | Moyen | 🟢 P3 |

### TL Voice Services International

| Automation | État | Effort setup | ROI | Priorité |
|------------|------|-------------|-----|----------|
| Onboarding flow 48h | Documenté | 6h (V2 auto) | Critique | 🔶 P2 |
| Vapi config templating | À créer | 2h | Haut (premier client) | 🔥 P1 |
| Voice catalog management | Framework | 2h | Moyen | 🔶 P2 |
| Customer success post-go-live | À créer | 2h | Haut | 🔶 P2 |

**Bloquage** : Pat doit signer Vapi/Twilio + sélectionner voices avant que toute automation devienne testable.

### TL KDP / Newsletter / Écriture

| Automation | État | Effort setup | ROI | Priorité |
|------------|------|-------------|-----|----------|
| Newsletter draft from topic + voice corpus | À créer | 3h | Haut | 🔥 P1 |
| Publer multi-platform publish | À créer (API) | 2h | Haut | 🔶 P2 |
| KDP draft outline → chapters | À créer | 4h | Moyen | 🔶 P2 |
| Voice corpus auto-enrich (sessions Pat) | À créer | 3h | Moyen | 🟢 P3 |

### TL Musique

Pas d'automation prévue. C'est le track perso de Pat.

### Patou-Overseer

| Automation | État | Effort setup | ROI | Priorité |
|------------|------|-------------|-----|----------|
| Scan 7 sources 2×/jour (9h + 20h) | ✅ Actif | — | Critique | ✅ |
| Journal Patou-Vault | ✅ Actif | — | Haut | ✅ |
| Alerte Telegram direct Pat | ✅ Actif | — | Critique | ✅ |
| Health check Claude principal (pour failover) | À créer | 2h | Haut | 🔥 P1 |
| Anomaly detection (volume, sentiment, errors) | À créer | 4h | Haut | 🔶 P2 |
| Briefing matinal 8h Pat (résumé 24h derniers) | Pup actif | — | Haut | ✅ |

---

## Top 5 automations à attaquer cette semaine (ROI immédiat)

1. **Hermès activation C1-C4** (débloquera 6 sous-automations) → attente API keys Pat
2. **Auto-draft response Upwork notifs** (Pat répond lentement, perte de leads) → 4h dev, debloque revenu freelance
3. **Customer success J+7/J+30 J4P** → 2h dev, lock retention pour lancement 9 juin
4. **Vapi config templating TL Voice** → 2h dev, accélère premier client receptionist
5. **Newsletter draft from topic** → 3h dev, lance newsletter sem 10 juin

**Total : ~13h de dev pour débloquer 5 axes de cash + retention.**

## Top 3 automations à éviter pour l'instant

1. **Auto-archive LinkedIn invitations** : trop tôt, Pat peut vouloir reviewer manuellement quelques uns
2. **YouTube thumbnail A/B auto-gen** : complexe, mieux Pat valide à la main jusqu'à 100k subs
3. **Voice corpus auto-enrich** : touche identité, mieux Pat décide quoi nourrir

## Stack technique automations

| Couche | Tech | Coût |
|--------|------|------|
| Orchestration | n8n (Mac local actuellement, → Beck juillet 2026) | $0 |
| Scheduler | LaunchAgent (Mac) + cron (Beck) | $0 |
| LLM brain | LiteLLM proxy → 11 modèles | inclus |
| Queue | Redis (à installer) ou simple JSONL files | $0 |
| Logs | JSONL + Patou-Vault | $0 |
| Monitoring | Patou-Overseer scans | $0 |

**Coût total stack automation** : $0/mo additionnel (utilise infra existante).

---

## Principe d'auto-évolution

Chaque automation déployée doit générer :
1. **Logs JSONL** dans `~/Linux/ops-control/data/` (auto-audit Patou)
2. **Métriques** dans `~/Linux/ops-control/data/automation-metrics.json`
3. **Endpoint health check** que Patou peut pinger

Si une automation passe en mode dégradé → Patou alerte Pat directement (pas via Claude).

---

## Décision Pat — quelles automations prioriser ?

**Option 1 — All-in cette semaine** : on attaque les 5 top automations en parallèle (~13h dev cumulé), Pat valide une par jour. Tu serais saturé 5 jours.

**Option 2 — Sequential, 1 par 2 jours** : on fait #1, validation Pat, on fait #2, etc. 10-12 jours pour le top 5. Moins de cognitive load Pat.

**Option 3 — Triage by blocker** : on fait d'abord celles qui débloquent revenu immédiat (Upwork auto-draft + Vapi templating + Newsletter), on attend pour le reste.

**Ma recommandation** : Option 3, focus revenue first. Les autres en V2.
