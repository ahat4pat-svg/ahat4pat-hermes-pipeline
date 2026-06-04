# TL Juniors4Pat — Team Leader AI Agents Sales B2B

> Department : Juniors4Pat (J4P)
> Lancement officiel : **lundi 9 juin 2026**
> Workflow source : Anti-Gravity Direct-to-Client B2B (Doc #2 NotebookLM)

## Vision

J4P = 225 produits AI-as-a-service prévus, prix $19-79/mois. Marché global. Phase 1 : OR pour LLM backend. Phase 2 : Gemma 4 local pour souveraineté coûts.

Produit phare initial : **Réceptionniste IA** (voix bilingue QC/EN-CA, Vapi + Twilio + LiteLLM stack).

## Stack

| Composante | Tool |
|------------|------|
| LLM backend | OpenRouter (Phase 1) → Gemma 4 local (Phase 2) |
| Voice | ElevenLabs (premium) + Qwen3-TTS (mass production) |
| Phone | Vapi + Twilio |
| Orchestration | Hermès sub-agent B2B + n8n flows |
| Memory client | Honcho + Vector Store (Chroma OR Qdrant) |
| Interface Pat → clients | Telegram bot J4P |
| Landing page | juniors4pat.com (Webflow OR Framer) |
| Payment | Stripe (déjà setup) |
| Tunnel | Cloudflare `webhook.juniors4pat.com` (déjà actif) |

## Pipeline livraison client (Zero-Touch)

```
1. Client signe-up via landing page → Stripe webhook
   ↓
2. Hermès sub-agent B2B reçoit notification (n8n flow)
   ├─ Crée project.json pour ce client
   ├─ Pull charte graphique client (logo, couleurs, voice tone)
   └─ Stocke dans Honcho Vector Store
   ↓
3. Onboarding automatique (1-2 days)
   ├─ Email welcome avec form questions
   ├─ Hermès personalise l'agent avec inputs client
   └─ Setup numéro Vapi + voice clone si premium tier
   ↓
4. Livraison agent (3-5 days)
   ├─ Test interne (Pat + Patou validation)
   ├─ Demo client via Telegram bot J4P
   └─ Activation production
   ↓
5. Maintenance ongoing
   ├─ Patou-Overseer monitore qualité réponses
   ├─ Hermès apprend des conversations client
   └─ Update mensuel automatique
```

## Tiers prix (à valider avec Pat avant 9 juin)

| Tier | Prix/mo | Cible | Inclus |
|------|---------|-------|--------|
| Starter | $19 | Solo entrepreneur | 1 agent simple, 100 conv/mois, voice générique |
| Pro | $49 | PME | 1 agent custom, voice clone, 500 conv/mois |
| Business | $79 | PME établie | 2 agents, voice clone premium, 2000 conv/mois, dashboard |
| Custom | sur devis | Enterprise | Multi-agents, intégration sur mesure, SLA |

## Tâches pré-lancement (avant 9 juin)

### Critiques (must-have)
- [ ] **Décision waitlist vs vente directe** sur landing page (Pat décide)
- [ ] Pat batch review 62 drafts Team B PME (= leads warm pour J4P)
- [ ] Outreach 2-3 pilot coachs (framing Priestley)
- [ ] Test Annie voice live (+1 826 334 9040)
- [ ] Activer Hermès sub-agent B2B dans pipeline

### Nice-to-have
- [ ] Demo vidéo réceptionniste IA en action (peut être C3 brief future)
- [ ] FAQ landing page
- [ ] Cas client #1 (même hypothétique pour démarrer)

## Sources de leads (Phase 1)

1. **Team B PME** drafts (62 ready, Pat à reviewer)
2. **Cross-promo C3 Stacklab** : vidéos AI tutorials mentionnent J4P
3. **Pilot coachs Priestley framing** (relation existante)
4. **Affiliate marketing** (déjà actif chez Pat)
5. **Reddit + LinkedIn outreach** (Hermès sub-agent scout)

## Métriques de succès (90 jours post-launch)

| Métrique | Cible mois 1 | Cible mois 3 |
|----------|--------------|--------------|
| Waitlist | 100+ | 500+ |
| Customers payants | 5-10 | 30-50 |
| MRR | $200-400 | $1500-3000 |
| Churn | < 10% | < 5% |
| NPS | 40+ | 60+ |

## Patou-Overseer checks

- Waitlist growth (alerte si pas growth 7 jours)
- Client delivery SLA (alerte si livraison > 5 jours)
- No drift from brief (livré conforme au pitch)
- Stripe webhook health
- Vapi/Twilio balance > $20

## Hermès sub-agent B2B — config (à créer)

Fichier : `tls/tl-juniors4pat/skills/j4p_client_onboarding.py`

Skills à implémenter :
- `create_client_project(client_data) -> project_id`
- `setup_vapi_agent(client_id, voice_id, language) -> agent_id`
- `customize_agent_personality(agent_id, brand_voice) -> bool`
- `monitor_agent_conversations(agent_id) -> metrics`
- `escalate_to_pat(agent_id, reason) -> notification_sent`

## Liens

- [[project_pat_junior4pat_vision_2026-05-20]] — vision long-terme J4P
- [[project_pat_ai_agents_sales_2026-06-02]] — pivot AI Agents Sales post-launch
- [[project_pat_voice_services_international_2026-06-02]] — voice services international (parallel TL)
