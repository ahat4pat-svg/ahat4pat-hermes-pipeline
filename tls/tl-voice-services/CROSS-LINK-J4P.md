# Cross-Link TL Voice Services × TL Juniors4Pat

> Comment les deux TLs s'imbriquent dans le portfolio AHat4Pat
> Verrouillé : draft 2026-06-04

---

## L'architecture conceptuelle

**TL Juniors4Pat = la vitrine de vente B2B + le hub commercial.**
**TL Voice Services = la production technique des produits voix.**

```
Client B2B
    │
    ▼
[J4P Landing / J4P Sales Pages] ◄── marketing, démos, témoignages
    │
    ▼
Décision achat → Stripe
    │
    ▼
[J4P Webhook receives payment]
    │
    ├──► [TL Voice Services Onboarding] ◄── tech delivery
    │    │
    │    └──► Annie configurée + déployée
    │
    └──► [J4P CRM] ◄── client lifecycle, billing, support
```

**TL Voice Services est invisible au client** — il voit juste « J4P livre ». Pat est le visage commercial (via J4P), TL Voice est l'usine.

## Produits J4P qui sortent de TL Voice Services

### Produit 1 — Réceptionniste IA (le hero)

**J4P vend** :
- Page de vente dédiée par secteur (4 versions : médical/dentaire/légal/immobilier)
- Démo audio + témoignages
- Calcul ROI interactif sur la landing (« combien de RDV perdus en 1 an ? »)
- 3 tiers : Starter 199$ / Pro 449$ / Business 899$ (per `pricing/structure-2026-06.md`)

**TL Voice livre** :
- Configuration Vapi
- Script secteur + customisation
- Voice choisie
- Intégrations calendrier/CRM
- Maintenance et updates

### Produit 2 — Voice Cloning service

**J4P vend** :
- Page courte « Clonez votre voix »
- Use cases : créateurs, podcasteurs, entreprises
- 3 tiers : Basique 499$ / Pro 999$ / Entreprise 2499$

**TL Voice livre** :
- Process clone ElevenLabs Pro
- Audio engineering / tuning
- Génération initiale + révisions
- Maintenance 12 mois (Entreprise)

### Produit 3 — Voice Over à la pièce

**J4P vend** :
- Page « Voice over québécoise + bilingue »
- Calculator de prix selon durée
- Portfolio audio (samples Pat ou catalog ElevenLabs sous licence)

**TL Voice livre** :
- Génération voice over
- Mix + mastering
- Livraison fichiers
- Révisions

### Produit 4 (futur, post-AI-Agents-Sales) — Voice Agents conversationnels

**J4P vend** :
- Voice agents pour commerce conversationnel
- Outbound calling (sales / qualification)
- Sondages clients automatisés

**TL Voice livre** :
- Architecture voice agent (Vapi outbound mode)
- Scripts adaptés au use case
- Intégrations CRM / e-commerce

---

## Flow opérationnel

### Lead arrive sur J4P landing

1. Lead remplit form intérêt OU achète directement
2. **Si form intérêt** : capture lead → email automatique → relance Pat sous 2h pour discovery call
3. **Si achat direct** : Stripe webhook → J4P CRM update → notification TL Voice → onboarding démarre

### Pendant onboarding (TL Voice prend le lead)

- TL Voice utilise `onboarding/flow-48h.md`
- Pat (en mode TL Voice) configure + teste
- Client validé → go live à 48h

### Post-onboarding (J4P reprend le lead)

- Client passe en mode « actif » dans J4P CRM
- Billing récurrent géré par Stripe (J4P)
- Support tier 1 (questions usage) géré par J4P
- Support tier 2 (bugs techniques) géré par TL Voice
- Upsell géré par J4P (relance email + check-in)

### Si client demande customisation profonde

- J4P collecte la demande, évalue scope
- Si <2h : TL Voice fait, no upsell
- Si 2-8h : devis à 79$/h, TL Voice fait après acceptation
- Si >8h : passage à tier supérieur ou projet custom

---

## KPIs partagés J4P × TL Voice

| KPI | Owner | Cible |
|-----|-------|-------|
| Leads / mois sur J4P landing | J4P | 50+ à 3 mois |
| Conversion lead → discovery call | J4P | 30% |
| Conversion discovery → vente | Pat | 40% |
| **Time-to-live (signature → Annie active)** | **TL Voice** | **<48h** |
| Churn rate mensuel | J4P (suivi) + TL Voice (qualité) | <5% |
| NPS clients | J4P (collecte) | >50 |
| Upsell rate à 90 jours | J4P | 30% |
| Référence rate à 6 mois | J4P | 25% |

---

## Risques cross-TL

### Risque 1 — TL Voice peut pas suivre la demande J4P

**Si J4P génère 30 leads/jour et TL Voice est solo Pat** → bottleneck.

**Mitigation** :
- Discovery call automatisable (Vapi outbound qualifiant le lead AVANT que Pat parle)
- Onboarding standardisable (V2 : sans Pat intervention pour Starter)
- Embauche partner technique si volume justifie

### Risque 2 — J4P promet ce que TL Voice peut pas livrer

**Risque concret** : J4P landing dit « live en 24h » alors que TL Voice fait 48h.

**Mitigation** :
- Single source of truth des SLA dans `pricing/structure-2026-06.md`
- J4P landing reprend EXACTEMENT ce que TL Voice peut livrer
- Aucune promesse marketing qui n'est pas dans le contrat tech

### Risque 3 — Branding confus côté client

**Risque** : client confus entre « J4P » et « TL Voice ».

**Mitigation** :
- **Le client ne voit que J4P (ou la marque que Pat décide)**. TL Voice est invisible.
- Tous les emails, factures, communications = brand J4P (ou autre brand)
- TL Voice est org interne, pas brand client-facing

---

## Évolution future

### Phase 1 (juin-août 2026) — Cash first

- TL Voice = Pat solo, manuel
- J4P landing simple + Stripe direct
- 3-5 pilot clients pour valider
- Cible : $2-5k MRR à fin août

### Phase 2 (sept-déc 2026) — Scale

- TL Voice = Pat + 1 partenaire technique OR automation onboarding
- J4P sales funnel optimisé (LinkedIn outreach + Annie qualifiante)
- 20-50 clients actifs
- Cible : $10-25k MRR à fin décembre

### Phase 3 (2027) — Diversification

- TL Voice ajoute voice agents avancés (commerce, sales outbound)
- J4P étend portfolio (AI agents non-voix sectoriels)
- Possibilité licence du produit white-label à d'autres agences

---

## Lien vers les autres docs TL Voice

- [README](README.md)
- [Vapi config base](vapi-config/receptionist-base.json)
- [Scripts par secteur](scripts/)
- [Pricing structure](pricing/structure-2026-06.md)
- [Onboarding flow](onboarding/flow-48h.md)
