# TL KDP / Newsletter / Écriture

> Team Leader · Publication écrite (newsletter, KDP, éventuellement Substack)
> Reports to : Claude (Director)
> Audité par : Patou-Overseer (independent)
> **État : équipe préparée 4 juin 2026 (deuxième team prep ce soir, après TL Voice)**

## Mission

Phase 2 mission incarnée — enseigner pour enlever de l'angoisse au monde — via publication écrite régulière.

- **Newsletter Décodeur IA en français** (lancement 10 juin 2026)
- **KDP livres courts** — premier titre : *Comprenez Claude en 30 pages* (draft 10-15 juin, publish fin juin)
- **Éventuellement Substack** (si newsletter prend traction, mirror pour audience anglo)

C'est la voix éditoriale de Pat. Le ton est verrouillé. La cadence est soutenable. L'objectif n'est pas le viral immédiat — c'est de bâtir un fil d'autorité authentique sur 6-12 mois.

## État (2026-06-04)

✅ **Préparé ce soir** :
- 3 templates newsletter (deep-dive / quick-tip / opinion)
- KDP outline complète (10 chapitres × ~700-900 mots)
- KDP format spec Kindle (Pandoc workflow + CSS + metadata)
- Pipeline publication Publer multi-plateforme documenté
- Cadence calendar 4 semaines de lancement (juin 2026)
- Cross-link avec voice corpus Pat
- 3 sujets prêts (déjà sur Desktop `FEUILLE-NEWSLETTER-2026-06-04.html`)

🔶 **Attente Pat / décision** :
- Choisir : Publer manuel vs API ($40 CAD tier supérieur si API utile)
- Valider outline KDP
- Cover KDP (Canva) à designer
- Pricing KDP à valider ($4.99 USD proposé)

🔴 **Prérequis avant publication #1 (10 juin)** :
- Newsletter #1 draftée et reviewed par Pat (sujet « L'idée est tout »)
- LinkedIn + X adaptations préparées
- Publer compte configuré avec scheduling

## Structure du dossier

```
tl-kdp-newsletter/
├── README.md                          ← ce fichier
├── templates/
│   ├── 01-deep-dive.md                ← format long, 1500-2200 mots
│   ├── 02-quick-tip.md                ← format court, 400-700 mots
│   └── 03-opinion.md                  ← format posture, 800-1200 mots
├── publication-pipeline/
│   └── publer-integration.md          ← flux multi-plateforme
├── kdp-comprenez-claude/
│   ├── 00-OUTLINE.md                  ← 10 chapitres détaillés
│   └── FORMAT-KINDLE-SPEC.md          ← Pandoc workflow + Kindle CSS
├── cadence/
│   └── publishing-calendar.md         ← rythme hebdo + lancement juin
├── issues/                            ← (drafts newsletters, à populer)
└── memory.md, project.json            ← état opérationnel
```

## Sous-agents Hermès (à activer)

| Sous-agent | Rôle | Modèle | Status |
|------------|------|--------|--------|
| `newsletter-drafter` | Écrit drafts newsletter en voix Pat (via templates) | DeepSeek V3.2 + voice corpus | scaffold |
| `newsletter-correcteur` | Vérifie style + image-first + auto-implication | Claude Sonnet | à créer |
| `newsletter-publisher` | Publie via Publer Pro (LinkedIn + X + FB + TikTok) | Publer API si tier upgrade | à créer |
| `kdp-drafter` | Écrit chapitres KDP en voix Pat | DeepSeek V3.2 + outline | à créer |
| `kdp-formatter` | Pandoc → epub/mobi pour Kindle | Pandoc + scripts | à créer |
| `social-adapter` | Adapte 1 source vers 4 versions (LinkedIn / X / FB / TikTok) | DeepSeek V3.2 | à créer |

## Stack publication

| Outlet | Plateforme | Coût |
|--------|-----------|------|
| Newsletter envoi | Publer Pro (intégration future) | $17/mo actif |
| Email principal | Newsletter dédiée OU intégrée Substack | $0 démarrage |
| KDP | Amazon Kindle Direct Publishing | gratuit, royalty 70% |
| Substack | (futur, semestre 2) | gratuit |
| Cross-promo X | Publer + X account Pat | $0 |
| Cross-promo LinkedIn | Publer + LinkedIn Patrick Lemieux | $0 |

## Voice & style (rappel verrouillé)

- **Auto-implication PURE** : « j'ai réalisé / j'ai vécu », jamais « vous devriez »
- **Image-first** : scène plantée AVANT pensée
- **Mise en situation style Le Soleil**, pas Journal de Québec
- **Influences** : Dostoïevski (intériorité), Balzac (détail concret)
- **Niveau lecteur** : pair, pas vulgariser
- **Tone** : pas coach, pas YouTuber tech, pas corpo. Voix Pat = quelqu'un qui a vécu et raconte.

Voice corpus complet : `~/.hermes/profiles/social/voice-corpus.md`

## Blockers actuels (en ordre de priorité)

1. **Pat valide outline KDP** (`kdp-comprenez-claude/00-OUTLINE.md`)
2. **Pat valide les 3 templates** (deep-dive / quick-tip / opinion) — sont-ils alignés ?
3. **Pat configure Publer scheduling** (15-20 min, accès UI existant)
4. **Pat décide pricing KDP** ($4.99 USD proposé)
5. **Cover KDP à designer** (Canva, ~1h Pat OU délégué à Claude pour brief)
6. **Newsletter #1 draftée** (sujet « L'idée est tout » prêt, draft à faire)

## Prochaine milestone

- **Semaine 10-14 juin** : Newsletter #1 envoyée + KDP draft à 50%
- **Semaine 17-21 juin** : Newsletter #2 + KDP draft 100%
- **Semaine 24-28 juin** : Newsletter #3 + KDP edit + cover + format
- **Fin juin / début juillet** : KDP publish sur Amazon + Newsletter #4 announce

## Métriques cibles

- **Newsletter subscribers** : 50 fin juin → 500 fin sept → 2000 fin 2026
- **KDP ventes** : 50-100 premier mois → 500 trois mois
- **Newsletter open rate** : 35%+ (baseline est 20-25%)
- **Click-through to action** : 5-8%

## Notes importantes

- **C'est Phase 2 (qualité-authenticité-enseigner)** appliquée. Pas Phase 1 cash direct.
- **Le revenu de ce TL n'est pas direct** — ce qu'il génère = autorité + leads pour J4P + leads pour Voice Services
- **Pat valide CHAQUE newsletter avant envoi** au moins pour les 10 premières (calibration voix)
- **Pas de growth-hacking sale tactics** — la cohérence éditoriale > clickbait
- **Lien avec voice clone** (`pat_custom`, à enregistrer demain) : version audio possible des newsletters

## Liens

- [ORG_CHART du repo principal](../../ORG_CHART.md)
- [Feuille Newsletter 2026-06-04 (Desktop)](../../../../../Desktop/FEUILLE-NEWSLETTER-2026-06-04.html)
- [Voice corpus Pat](../../../../.hermes/profiles/social/voice-corpus.md)
- [TL J4P pour cross-promo produits](../tl-juniors4pat/README.md)
- [TL Voice Services pour audio version newsletters](../tl-voice-services/README.md)
