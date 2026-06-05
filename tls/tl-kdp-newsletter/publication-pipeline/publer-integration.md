# Pipeline publication — Publer Pro multi-plateforme

> Service : Publer Pro ($16.56 CAD/mo, re-souscrit 2 juin 2026)
> Plateformes couvertes : LinkedIn + X + Facebook + TikTok (à venir)
> Use case primaire : newsletter Décodeur IA en français + posts Pat personnels

## État Publer 2026-06-04

- ✅ Compte Pro actif
- 🔶 LinkedIn connecté (à vérifier)
- 🔶 X connecté (à vérifier)
- 🔶 Facebook : à connecter
- 🔶 TikTok : à connecter

## Architecture du flux de publication

```
Topic identifié (voice corpus Pat / actu IA / réflexion Phase 2)
    ↓
Brief MD (1 page max)
    ↓
Newsletter drafter (Hermès skill — voix Pat verrouillée)
    ↓
Pat reviews (15 min)
    ↓
Adaptations par plateforme :
    ├─ LinkedIn (1500-3000 caractères, voix pro mais perso)
    ├─ X / thread (5-10 tweets, hook-driven)
    ├─ Facebook (cross-post LinkedIn + image)
    ├─ TikTok (script vidéo 60-90 sec, scénarisé pour Pat)
    └─ Newsletter email (version complète 800-1500 mots)
    ↓
Publer planifie tout en burst coordonné
    ↓
Tracking engagement (Publer analytics + Bitly URLs)
```

## Adaptations par plateforme

### LinkedIn (voix pro avec personnalité)

- **Longueur** : 1500-3000 caractères (sweet spot algo)
- **Structure** : Hook (1 ligne forte) → contexte (2-3 lignes) → meat (paragraphes courts) → CTA discret
- **Format** : phrases courtes + retours à la ligne fréquents (mobile-first)
- **Image** : visuel custom OU snippet de la newsletter
- **Hashtags** : 3-5 max, fin du post, pas inline
- **Best time post** : 8h-10h ou 17h-19h jours ouvrables

### X / Twitter (thread)

- **Format** : thread 5-10 tweets
- **Tweet 1** : hook + promise du thread
- **Tweets 2-N** : 1 idée par tweet, 200-260 caractères
- **Dernier tweet** : CTA + lien newsletter
- **Best time post** : matin tôt 7h-9h ET soirée 18h-21h

### Facebook (cross-post + visuel)

- **Stratégie minimum** : cross-post LinkedIn + image accrocheuse
- **Audience plus large mais moins engagée que LinkedIn** pour cette niche
- **Best time post** : midi 11h-13h ou soirée 19h-21h

### TikTok (vidéo scénarisée)

- **Format** : 60-90 sec, Pat parle face caméra OU faceless avec voix Pat
- **Hook 3 sec** : phrase qui claque
- **Meat 45-75 sec** : 1 idée concrète + démo si possible
- **CTA 5-10 sec** : « follow pour plus » + lien bio newsletter
- **Note D2** : si Pat veut rester anonyme côté TikTok, utiliser voice Pat sur faceless visuels

### Newsletter email (version complète)

- **Format** : 800-1500 mots
- **Voix Pat verrouillée** : auto-implication PURE + image-first + style Le Soleil
- **Structure** : scène (image plantée) → réflexion (j'ai réalisé) → question ouverte → bonus pratique
- **CTA** : selon le sujet (achat produit J4P, KDP, ou rien si éditorial pur)
- **Désabonnement** : un lien clair (loi anti-spam Canada)

## Workflow tools

### Option 1 — Manuel via Publer UI (Phase 1 cash)

1. Pat ou Claude rédige les 5 versions (newsletter + 4 adaptations sociales)
2. Connexion à publer.com
3. Création post pour chaque plateforme avec scheduling
4. Burst coordonné planifié

### Option 2 — Publer API (Phase 2 automation)

Publer offre une API pour les comptes Business+ (à vérifier si Pro inclut, sinon upgrade $40 CAD/mo).

```python
# Pseudocode flow
publer.post(
    platform="linkedin",
    content=adapt_for_linkedin(article_md),
    schedule_at="2026-06-10T08:30:00-04:00",
    media=[generated_image_path]
)
```

À explorer si volume de publication dépasse 10/semaine.

## Métriques à tracker

| Métrique | Cible début | Cible 3 mois |
|----------|-------------|--------------|
| Subscribers newsletter | 0 → 50 | 500+ |
| LinkedIn followers gain/mois | 50 | 200+ |
| X followers gain/mois | 30 | 150+ |
| Engagement rate moyen LinkedIn | 3% | 5%+ |
| Click-through newsletter → site | 5% | 12%+ |
| Conversion newsletter → produit J4P | 1% | 3%+ |

## Intégration avec autres TLs

- **TL Faceless YT** : vidéos YouTube → snippets pour LinkedIn + X (cross-promo organique)
- **TL J4P** : produits J4P mentionnés dans newsletters (sans vendre fort)
- **TL Voice Services** : cours/tutoriels IA dans newsletter = lead magnet pour services
- **TL KDP** : extracts du livre dans newsletter = pre-launch hype

## Risques

- **Algorithme LinkedIn change** : éviter de devenir trop dépendant d'un seul canal
- **TikTok bannit / change** : avoir un fallback (Instagram Reels, YouTube Shorts)
- **Burnout création** : volume soutenable = 2-3 posts/semaine, pas plus
- **Voix Pat dérive** : si auto-generation, audit régulier par Pat pour garder l'authenticité

---

*À valider par Pat : si Publer API n'est pas dans le tier Pro, on reste manuel jusqu'à volume justifiant upgrade.*
