# Workflow C1 Stillcraft — Storytelling Visuel

> Channel : C1 Stillcraft · format long-form 10-15 min horizontal 16:9
> Voix : narration ElevenLabs (voice TBD parmi catalogue Pat, jamais default)
> Production cible : 1-2 vidéos/semaine
> Anonyme — pas de face, pas voix Pat directe (D2 channel)

## Concept

Storytelling cinématique — récits humains, anthropologiques, philosophiques. Slow burn, image-first, narration en voix-off posée. Inspirations : Kurzgesagt (rythme + science) × Wendover Productions (récit géopolitique) × Patrick Boucheron (regard historien) × Nuit blanche cinéma québécois.

Sujets cibles :
- Récits anthropologiques (rituels, gestes, métiers oubliés)
- Histoires d'objets (la fourchette, la clé, le marteau)
- Mini-biographies de figures oubliées (Québec + monde)
- Méditations sur des phénomènes (la patience, la promesse, le silence)
- Petites histoires de l'humanité face à la technologie

## Stack technique

| Étape | Tool | Note |
|-------|------|------|
| Script | Claude Opus 4.7 | prompt long-form storytelling, structure 3 actes |
| Voice | ElevenLabs `eleven_multilingual_v2` voice neutre choisie | speaking_rate 0.95-1.05 (posé) |
| Visuels (B-roll) | Pexels + Pixabay archive + footage libres | 60% archive / 40% IA |
| Visuels (IA) | Higgs Field Seedance 2.0 + FLUX.2 | scènes hero rare, atmosphères |
| Édition | Remotion (templates programmatiques) | composition image-first |
| Sous-titres | Whisper transcription → Burney karaoké | mot actif accent doré (Stillcraft palette) |
| Stitch | ffmpeg `-shortest` | flag impératif |
| Musique | Epidemic Sound OR royalty-free curated | ambient/cinematic, low frequency dominant |

## Pipeline Hermès

```
1. Brief MD validé Pat
   ↓
2. c1-storytelling-writer (Hermès skill)
   ├─ recherche sources primaires (3 minimum)
   ├─ structure 3 actes : situation → tension → résolution/ouverture
   ├─ génère script 1500-2200 mots ton narrateur posé
   └─ inclut chapters + description 500+ mots + tags
   ↓
3. generate_voiceover (Hermès tool)
   ├─ voice_id neutre catalogue Pat
   ├─ speaking_rate 1.0
   ├─ balises pauses respirées entre paragraphes
   └─ pauses dramatiques avant chaque pivot d'acte
   ↓
4. fetch_stock_assets (Hermès tool, parallel)
   ├─ 15-25 clips Pexels/Pixabay (archive + nature + textures)
   ├─ 3-5 scènes Seedance hero (atmosphères clés)
   └─ FLUX still frames pour titres/cartons
   ↓
5. remotion-render (Hermès skill)
   ├─ composition image-first : visuel respire AVANT le mot
   ├─ transitions lentes (cross-fade 1.5s, pas cut sec)
   ├─ overlay voice + musique 35% volume max
   └─ output MP4 H.264 1080p
   ↓
6. youtube-uploader (Hermès skill)
   ├─ upload via YouTube Data API
   ├─ chapters dans description (1 par acte minimum)
   ├─ transcript manuel uploadé (PAS auto-caption)
   ├─ thumbnail custom (cinema-still aesthetic)
   └─ ping Patou-Overseer pour audit post-publish
```

## Voice narratoriale — règles de production

### Posture
- Narrateur omniscient mais humble — pas oracle, plutôt témoin
- Phrases longues qui déroulent + courtes coupes pour impact
- Pauses respirées entre paragraphes (4-5 sec, pas 3 comme C3)
- Speaking rate 1.0 standard, 0.95 pour passages contemplatifs
- JAMAIS default voices ElevenLabs
- Voix sélectionnée doit pouvoir tenir 12 min sans fatiguer l'oreille

### Énergie
- Basse à moyenne, jamais haute
- Modulation par contraste rythmique, pas par volume
- Climax = ralentissement, pas explosion
- Closing = note ouverte (question, image, silence chargé)

### Structure narrative
- **Acte 1 (3 min)** : situer un détail concret, planter le mystère
- **Acte 2 (6-8 min)** : déployer la complexité, multiplier les angles
- **Acte 3 (2-3 min)** : résoudre OU ouvrir vers plus grand, jamais conclure didactique

## SEO / GEO (règles Romayroh strictes)

- **Long-form 10-20 min** (sweet spot 12-15 min)
- **Chapters dans description** : minimum 5 (acte 1, pivot, acte 2 sections, climax, ouverture)
- **Description 500+ mots** avec entités historiques nommées (lieux, dates, personnes)
- **Transcript manuel uploadé** via YT Studio (règle absolue)
- **Tags** : storytelling, histoire, anthropologie, [topic-specific], documentaire court, récits, narration
- **Title A/B** : un titre intrigant + un titre informatif, alterner

## Différence avec C2 Loopkeeper

- **C1 Stillcraft = un récit unique focalisé** (1 histoire, 12 min, image-first cinéma)
- **C2 Loopkeeper = swarm documentaire long** (sujet décomposé en multiples angles agents, 20-40 min, recherche-first)

## Monétisation

### Phase 1 (0-1000 subs)
- Affiliate links dans description (livres + outils contemplatifs)
- Mentions naturelles (éditions, instruments cités)
- Bitly cleanup

### Phase 2 (1000+ subs + 4000 watch hours)
- YouTube Partner Program activé
- Sponsors compatibles avec ton posé (Masterclass, Squarespace, etc.)
- Patreon possible (audience contemplative aime ça)

### Phase 3 (10k+ subs)
- Audiobook narration commercial (voix sélectionnée + style établi = asset vendable)
- Podcast adapté (audio-only deploy)

## Métriques de succès

| Période | Cible vues moyenne | Cible subs | Cible AVD | Cible CTR |
|---------|--------------------|-----------|-----------|-----------|
| Sem 1-2 | 300-1500 | 50-200 | 5 min | 3% |
| Mois 1 | 3000-10000 | 500+ | 7 min | 5% |
| Mois 3 | 20000+ | 5000+ | 9 min | 7% |
| Mois 6 | 80000+ | 30000+ | 10+ min | 9%+ |

Note : C1 a un CTR cible plus bas que C3 mais une AVD plus haute. L'algo aime ça pour le watch time absolu.

## Brief template (référence : 06 dans channels/c1-stillcraft/briefs/)

Structure obligatoire :
1. Hook visuel (15-20 sec) — image qui captive AVANT le premier mot
2. Promise / Tension (30 sec) — le mystère à résoudre
3. Acte 1 (3 min) — contexte historique/anthropologique
4. Acte 2 (6-8 min, 3-4 sections) — déploiement
5. Acte 3 (2-3 min) — résolution/ouverture
6. Closing image + question — 20 sec, silence laissé
7. CTA discret + Liens
8. Métadonnées (titre, chapters, description 500+, tags)
9. Critères qualité (anti-slop : pas de raccourcis IA visibles, pas de tutoriel ton, pas d'urgence)
10. Production estimée

## Patou-Overseer scan

- Voice quality check : voice_id != default ElevenLabs
- Speaking rate compliance : 0.9-1.1 (plus bas que C3)
- SEO compliance : chapters + description 500+ mots + manual transcript
- AVD à 24h post-publish : si <40% du runtime → alerte
- Cadence : 1-2 vidéos/semaine
- D2 compliance : pas voix Pat, pas face Pat — channel anonyme verrouillé
