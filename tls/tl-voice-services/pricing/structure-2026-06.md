# TL Voice Services — Structure de prix v1.0

> Verrouillé : draft 2026-06-04, à approuver par Pat
> Devise : CAD (sauf voice over international = USD)
> Marché cible primaire : Québec PME (médical, dentaire, légal, immobilier)
> Marché cible secondaire : International EN (voice over, podcast narration)

---

## Tier 1 — AI Receptionist Mensuel

**Le cash-cow récurrent — Phase 1 mission directe.**

### Starter — 199 $/mois

- 1 secteur prédéfini (médical / dentaire / légal / immobilier)
- Script standard (un des 4 fournis)
- Heures bureau (8h-18h) + voicemail après heures
- Jusqu'à 200 appels/mois
- 1 numéro local Twilio inclus
- Onboarding 48h
- Email support
- **Cible** : solo médecin, dentiste solo, courtier solo

### Professional — 449 $/mois (recommandé)

- Tout Starter +
- 24/7 (pas juste heures bureau)
- Jusqu'à 600 appels/mois
- Personnalisation script (jusqu'à 4h conseils)
- Intégration calendrier (Google/Outlook/CRM)
- Notifications SMS instantanées
- Dashboard analytics simple
- Phone support
- **Cible** : clinique 2-4 médecins, cabinet boutique 2-5 avocats, agence immobilière équipe

### Business — 899 $/mois

- Tout Professional +
- Appels illimités
- Multi-script (jusqu'à 3 scripts différents — ex : ligne principale + ligne urgence + ligne admin)
- Voice cloning (voix custom propre à l'entreprise)
- Intégration CRM avancée (lookup en temps réel des dossiers)
- Conformité renforcée (logs chiffrés, audit trails)
- Account manager dédié
- **Cible** : clinique 5+ médecins, cabinet 5+ avocats, agence immobilière franchise

### Setup fee (one-shot)

- **149 $** par activation, peu importe le tier
- Couvre : config Vapi + script adaptation + tests + porting numéro

### Add-ons

- **Voix personnalisée premium** (voice clone propriétaire) : +99 $/mois
- **Bilingue FR/EN** : +49 $/mois
- **Numéro supplémentaire** : +15 $/mois par numéro
- **Intégration CRM custom** (au-delà des intégrations standard) : devis sur mesure
- **Heures bureau étendues** (jours fériés inclus) : +29 $/mois

---

## Tier 2 — Voice Over Services (one-shot)

**Pour le marché EN/US/global — voix Pat ou voix catalogue.**

### Tarification à la pièce (CAD pour QC, USD pour international)

| Type | Durée | Prix CAD | Prix USD intl |
|------|-------|----------|---------------|
| Publicité radio/web courte | <30 sec | 149$ | 119$ |
| Publicité longue / pub TV | 30-60 sec | 249$ | 199$ |
| Narration corporative | 1-3 min | 499$ | 399$ |
| Narration longue (e-learning, audiobook) | 3-10 min | 1.49$ / mot | 1.19$ / mot |
| Narration audiobook complet | >1h | Devis sur mesure | Devis sur mesure |

**Inclus dans tous les voice over** :
- 2 prises (la livraison initiale + 1 révision)
- Format audio livré : WAV 48kHz 24-bit + MP3 320kbps
- Droits commerciaux pour usage spécifié

**Add-ons** :
- Révision additionnelle (au-delà des 2 prises) : 49$
- Mastering audio + mix musique : 79$
- Livraison express <24h : +50% du tarif de base

---

## Tier 3 — Voice Cloning (one-shot)

**Permet à un client de cloner sa propre voix pour ses propres usages.**

### Clone basique — 499 $

- 30 min d'audio source du client requis
- Voice clone ElevenLabs Pro
- 10 000 caractères de génération inclus (~1 200 mots)
- 1 révision incluse
- **Cible** : créateur de contenu solo, podcaster, entrepreneur visible

### Clone professionnel — 999 $

- 60+ min d'audio source
- Voice clone optimisé (multiple voice samples + tuning)
- 50 000 caractères de génération inclus (~6 000 mots)
- 3 révisions
- Live test avec exemples avant livraison finale
- **Cible** : entreprise, cabinet, marque

### Clone entreprise — 2 499 $

- Voix custom propriétaire (le client garde la voix exclusive)
- Multi-styles (lecture, vente, conversationnel)
- 200 000 caractères de génération inclus
- Maintenance & ajustements pendant 12 mois
- **Cible** : entreprise qui veut une voix de marque dédiée

### Add-ons Cloning

- Caractères supplémentaires : 0.02$/caractère après inclus
- Voix bilingue (FR + EN) : +199$
- Maintenance annuelle après 12 mois : 299$/an

---

## Discounts

- **Annual prepay** (12 mois payés d'avance) : -10%
- **Multi-tier bundle** (Receptionist Professional + Voice over package) : -15% sur le second tier
- **Pilot partner** (3 premiers clients par secteur) : -25% les 3 premiers mois
- **Référence client** : 1 mois gratuit pour le référent ET 1 mois gratuit pour le nouveau

---

## Économie unitaire (analyse)

### AI Receptionist Professional ($449/mo) — coûts mensuels estimés

- ElevenLabs (génération voix par appel) : ~$15/mo pour 600 appels
- Vapi (orchestration) : ~$30/mo pour 600 appels
- Twilio (telephony + numéro) : ~$25/mo (numéro $1 + ~$0.013/min)
- Anthropic Claude (Sonnet) brain : ~$10/mo
- Modal/infra : amorti $5/mo
- **Total coûts variables** : ~$85/mo
- **Marge brute** : ~$364/mo (81%)

À 10 clients Professional : revenu $4 490/mo, coût ~$850/mo, **marge $3 640/mo**.
À 50 clients : revenu $22 450/mo, coût ~$4 250/mo, **marge $18 200/mo**.

### Voice Over (one-shot $499 narration corporative)

- ElevenLabs génération + mastering temps : ~$2 coût direct
- Temps Pat (revision + QA) : 30 min
- **Marge brute** : $497 quasi-pur

---

## Notes Pat

- **Tarifs Receptionist agressifs vs marché** : compétition US (PolyAI, Hey Vern) à $500-$3000/mo Starter. On entre à $199 pour démontrer + monter rapidement les clients sur Professional/Business.
- **Voice over compétitif vs Voices.com / Voquent** : on est légèrement sous le marché EN/US pour gagner du share, on monte les prix après 30-50 clients réussis.
- **Voice cloning** : marché jeune, prix volatile. $499-$2499 est dans la fourchette ElevenLabs Pro service direct, on ajoute la valeur du service complet.
- **Importance du pilot partner discount** : les 3 premiers de chaque secteur = études de cas + témoignages → marketing organique.
- **Compatible avec J4P** : ce TL alimente directement J4P (J4P vend les receptionists + autres agents, TL Voice les construit/maintient).

---

## Prochaines actions

1. **Pat approuve / ajuste les tiers**
2. **Mettre les pages de vente live** (intégrer dans J4P landing)
3. **3 pilot partners signés à -25%** comme stretch goal pour la première semaine de juin
4. **Premier client payant à tarif plein** = objectif fin juin
