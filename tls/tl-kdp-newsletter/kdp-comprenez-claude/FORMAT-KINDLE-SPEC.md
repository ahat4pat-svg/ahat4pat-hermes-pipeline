# KDP Format Spec — Comprenez Claude en 30 pages

> Spec technique pour formatter le livre vers Kindle (epub/mobi)
> Workflow : Markdown → Pandoc → epub → Kindle Previewer → Upload KDP

## Stack technique

```bash
# Install requis
brew install pandoc
brew install --cask kindle-previewer
```

## Structure de fichiers

```
kdp-comprenez-claude/
├── 00-OUTLINE.md
├── FORMAT-KINDLE-SPEC.md           ← ce fichier
├── manuscript/
│   ├── 00-frontmatter.md           ← titre, copyright, dédicace
│   ├── 01-introduction.md
│   ├── 02-ce-que-claude-est.md
│   ├── 03-conversation-matiere.md
│   ├── ...
│   ├── 10-bonus.md
│   └── 99-annexes.md
├── assets/
│   ├── cover-final.png             ← 1600x2560 px (KDP standard)
│   ├── cover-source.canva.link
│   └── (zéro autre image inline pour éviter problèmes formatting)
├── metadata.yaml                    ← métadonnées pour Pandoc
└── build/
    ├── comprenez-claude.epub       ← output Pandoc
    └── comprenez-claude.mobi       ← optionnel (legacy)
```

## metadata.yaml

```yaml
---
title: "Comprenez Claude en 30 pages"
subtitle: "Un guide honnête pour utiliser l'IA d'Anthropic sans bullshit"
author: "Patrick Lemieux"
publisher: "AHat4Pat"
date: "2026-06"
rights: "© 2026 Patrick Lemieux. Tous droits réservés."
language: "fr-CA"
description: |
  18 mois après avoir commencé à utiliser Claude tous les jours,
  Patrick Lemieux livre un guide honnête : ce que l'outil est vraiment,
  comment l'intégrer à son travail sans devenir dépendant, et les pièges
  qu'il a appris à ses dépens. Pas un manuel technique. Pas un cours de
  prompting. Un livre court pour quelqu'un qui veut comprendre pourquoi
  cet outil change quelque chose.
keywords: ["Claude AI", "Anthropic", "IA", "productivité", "outils IA", "ChatGPT alternative"]
cover-image: "assets/cover-final.png"
---
```

## Pandoc commands

### Génération epub

```bash
cd ~/Linux/faceless-yt/pipeline/tls/tl-kdp-newsletter/kdp-comprenez-claude/

pandoc \
  --from=markdown \
  --to=epub3 \
  --output=build/comprenez-claude.epub \
  --metadata-file=metadata.yaml \
  --epub-cover-image=assets/cover-final.png \
  --toc \
  --toc-depth=2 \
  --split-level=1 \
  --css=assets/kindle-style.css \
  manuscript/*.md
```

### Génération mobi (legacy, optionnel)

```bash
# Kindle accepte epub maintenant, mais mobi reste safe fallback
kindlegen build/comprenez-claude.epub
```

## CSS minimal pour Kindle (assets/kindle-style.css)

```css
/* Kindle-optimized — minimal, robust across devices */
body {
  font-family: serif;
  line-height: 1.6;
  margin: 0;
  padding: 0;
}

h1 {
  font-size: 1.8em;
  font-weight: bold;
  margin-top: 2em;
  margin-bottom: 0.5em;
  page-break-before: always;
}

h2 {
  font-size: 1.4em;
  font-weight: bold;
  margin-top: 1.5em;
  margin-bottom: 0.3em;
}

h3 {
  font-size: 1.2em;
  font-weight: bold;
  margin-top: 1.2em;
}

p {
  margin: 0.5em 0;
  text-indent: 0;
}

blockquote {
  margin-left: 1em;
  font-style: italic;
  border-left: 3px solid #ccc;
  padding-left: 0.8em;
}

code {
  font-family: monospace;
  background-color: #f4f4f4;
  padding: 2px 4px;
}

/* No images inline — keep small file size */
img { display: none; }
```

## Validation avant publish

1. **Ouvrir dans Kindle Previewer** :
   ```bash
   open -a "Kindle Previewer 3" build/comprenez-claude.epub
   ```
2. Vérifier rendering iPhone + iPad + Kindle Paperwhite preview
3. Tester table des matières navigable
4. Vérifier qu'il n'y a pas de mots coupés bizarrement
5. Tester le saut de chapitre (1 chapitre = 1 page)

## KDP Upload

### Métadonnées à remplir sur kdp.amazon.com

- **Title** : « Comprenez Claude en 30 pages »
- **Subtitle** : « Un guide honnête pour utiliser l'IA d'Anthropic sans bullshit »
- **Author** : Patrick Lemieux
- **Description** : (~ 1500 caractères max, SEO-friendly)
- **Keywords** (7 max) : claude ai, intelligence artificielle, anthropic, IA productivité, chatgpt alternative, outils IA français, IA débutant
- **Categories** (2 sélections) :
  - Computers & Technology > AI & Semantics
  - Self-Help > Productivity (ou Business > Technology Industry selon angle)
- **Audience** : 18+ (default, pas de raison de restreindre)
- **Pricing** :
  - $4.99 USD (royalty 70%)
  - $6.99 CAD
  - $4.79 EUR
- **Distribution** : Worldwide
- **DRM** : OFF (Pat préfère pas de DRM — philosophiquement cohérent avec « pas dépendant des big tech »)

## Cover spec

- **Dimensions** : 1600 × 2560 px (KDP standard)
- **Format** : PNG ou JPG (PNG préférable, qualité meilleure)
- **DPI** : 300
- **Couleurs** : RGB
- **Outils suggérés** : Canva (template Book Cover Kindle) — PAS image IA générée (Pat veut une cover qui respecte le contenu)
- **Style** : sobre, typographique fort, palette 2-3 couleurs max
- **À ÉVITER** : générique tech IA (réseaux neuronaux bleus, cerveau pixelisé, robot)

## Cross-promo plan post-publish

- Newsletter envoie une mention dans #1 et #2
- Post LinkedIn (1500-3000 caractères) avec scène réelle de pourquoi le livre
- Post X / thread (10 tweets, 1 extrait par chapitre)
- Mentions discrètes dans les vidéos C3 Stacklab (« j'en parle plus en détail dans mon livre, lien en description »)

## Métriques de succès

| Métrique | Cible 30j | Cible 90j |
|----------|-----------|-----------|
| Ventes | 50-100 | 200-500 |
| Reviews (4★+) | 5-10 | 20-50 |
| Revenu KDP | $175-350 | $700-1750 |
| Leads newsletter via livre | 20-50 | 100-200 |
| Leads J4P via livre | 5-15 | 30-60 |
