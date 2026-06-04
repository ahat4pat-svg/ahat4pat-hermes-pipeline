# Workflow C2 Loopkeeper — Documentaires Longs Swarm

> Channel : C2 Loopkeeper · format ultra-long 20-40 min horizontal 16:9
> Voix : narration ElevenLabs (voice TBD, différent de C1 Stillcraft)
> Production cible : 1 vidéo/semaine, parfois bi-hebdo
> Anonyme — pas de face, pas voix Pat directe (D2 channel)
> Méthode : agentic swarm — multiples sous-agents recherchent en parallèle, un sous-agent synthétise

## Concept

Documentaires longs investigateurs sur sujets complexes — chaque vidéo = 4-8 angles parallèles documentés par sous-agents Hermès, synthétisés par un sub-agent éditorial.

Sujets cibles :
- Phénomènes contemporains complexes (TikTok shop economics, AI labor displacement, crypto regulation patchwork)
- Histoires longues à plusieurs branches (la cigarette du XXe siècle, le sucre, le plastique)
- Conflits géopolitiques avec angles méconnus
- Industries opaques (logistique maritime, semiconducteurs, médicaments génériques)
- Mouvements de pensée trans-décennaux (transhumanisme, decroissance, libéralisme)

Le « long » est essentiel — YouTube favorise les 30+ min pour watch time. C2 vise le binge.

## Stack technique

| Étape | Tool | Note |
|-------|------|------|
| Recherche | 4-8 sous-agents Hermès parallèles | chacun un angle, sources primaires |
| Synthèse | sub-agent `loopkeeper-editor` | merge angles, structure narrative |
| Script | Claude Opus 4.7 | prompt long-form documentaire, 3000-5000 mots |
| Voice | ElevenLabs `eleven_multilingual_v2` voice journalistic | speaking_rate 1.0 (posé documentaire) |
| Visuels (B-roll archive) | Pexels + Wikimedia Commons + footage libres + screen recordings | 70% archive |
| Visuels (data viz) | D3.js OR Datawrapper exports | graphiques + maps + timelines |
| Visuels (IA hero) | Higgs Field Seedance + FLUX | parcimonieux, 2-4 scènes max |
| Édition | Remotion (templates) + post CapCut | composition data-first |
| Sous-titres | Whisper transcription → Burney karaoké | mot actif accent vert (Loopkeeper palette) |
| Stitch | ffmpeg `-shortest` | flag impératif |
| Musique | Epidemic Sound | doc/investigative cues, alternance tension/calme |

## Pipeline Hermès — méthode SWARM

```
1. Brief MD validé Pat (sujet + angles initiaux)
   ↓
2. loopkeeper-coordinator (Hermès skill)
   ├─ décompose le sujet en 4-8 angles indépendants
   ├─ assigne chaque angle à un sub-agent
   └─ établit le timeline cible
   ↓
3. FORK : 4-8 sub-agents en parallèle (Fork and Run pattern)
   ├─ research-agent-1 : angle économique
   ├─ research-agent-2 : angle historique
   ├─ research-agent-3 : angle technique
   ├─ research-agent-4 : angle géopolitique
   ├─ research-agent-5 : angle humain/portraits
   ├─ research-agent-6 : angle critique/contre
   ├─ research-agent-7 : angle prospectif
   └─ research-agent-8 : angle culturel/médiatique
   chaque agent :
   ├─ utilise WebSearch + WebFetch + source databases
   ├─ produit synthèse 800-1500 mots + sources citées
   └─ flag les points sensibles/débattus
   ↓
4. JOIN : loopkeeper-editor (Hermès skill)
   ├─ merge 4-8 syntheses
   ├─ détecte contradictions entre angles → les transforme en tension narrative
   ├─ structure script 5 actes (situation, complexification, conflit, climax, ouverture)
   └─ produit script final 3000-5000 mots
   ↓
5. generate_voiceover (Hermès tool)
   ├─ voice neutre journalistic
   ├─ speaking_rate 1.0
   ├─ balises pauses entre actes (5 sec)
   └─ accents toniques sur entités nommées et chiffres
   ↓
6. data-viz-generator (Hermès skill, parallel à 5)
   ├─ génère graphiques D3/Datawrapper
   ├─ exporte PNG/SVG transparent background
   └─ timecode-aligned avec script
   ↓
7. remotion-render (Hermès skill)
   ├─ compose : B-roll + data viz overlay + voice + musique
   ├─ chapters visibles dans la timeline (intertitres)
   ├─ overlay musique 25% volume (plus bas que C1)
   └─ output MP4 H.264 1080p
   ↓
8. youtube-uploader (Hermès skill)
   ├─ upload via YouTube Data API
   ├─ chapters dans description (1 par acte + sous-sections)
   ├─ transcript manuel uploadé
   ├─ thumbnail custom (doc/investigative aesthetic, texte minimal)
   ├─ pinned comment avec liens sources principaux
   └─ ping Patou-Overseer pour audit post-publish
```

## Voice narratoriale — règles de production

### Posture
- Journaliste-narrateur, pas militant — multiples angles présentés équitablement
- Phrases factuelles courtes + transitions analytiques
- Pauses entre actes (5 sec, soulignées musicalement)
- Speaking rate 1.0 — pas plus haut (le sujet est dense, l'auditeur a besoin de respirer)
- JAMAIS default voices ElevenLabs
- Voix différente de C1 Stillcraft (audience peut suivre les deux sans confusion)

### Énergie
- Constante, pas de pic émotionnel
- Modulation par la cadence des chiffres + entités nommées
- Climax = révélation/connection majeure, pas drama
- Closing = état des lieux + invitation à approfondir (pas conclusion fermée)

### Citation des sources
- À chaque chiffre majeur : source nommée dans le voice + dans le subtitle
- Sources controversées : explicitement présentées comme telles
- Sources primaires > secondaires (toujours)

## SEO / GEO (règles Romayroh strictes + spécificités doc)

- **Long-form 20-40 min** (sweet spot 25-30 min)
- **Chapters dans description** : minimum 8 (5 actes + sous-sections)
- **Description 800+ mots** (plus que C1/C3 — sujet complexe)
- **Transcript manuel uploadé** via YT Studio (règle absolue)
- **Tags** : documentaire, investigation, [topic-specific], analyse, géopolitique/économie/histoire, long-form
- **Title** : informatif ET intrigant — pas clickbait pur (l'audience doc déteste ça)
- **Thumbnail** : aesthetic doc/investigative, texte court ou nul, image archive forte
- **Pinned comment** : liens sources clés, invitation à la discussion

## Différence avec C1 Stillcraft

- **C1 Stillcraft = un récit unique focalisé** (1 angle, 12 min, image-first cinéma)
- **C2 Loopkeeper = swarm documentaire long** (4-8 angles, 30 min, recherche-first, méthode agentic explicitée)

## Monétisation

### Phase 1 (0-1000 subs)
- Affiliate links sources/livres dans description
- Mentions naturelles d'outils analytiques (Datawrapper, etc.)
- Bitly cleanup

### Phase 2 (1000+ subs + 4000 watch hours)
- YouTube Partner Program activé
- AdSense premium (long-form = mid-roll multiples = revenue $$$)
- Sponsors investigative-compatible (Brilliant, Audible, Ground News)

### Phase 3 (10k+ subs)
- Premium paid documentary versions (60-90 min extended cuts sur Patreon)
- Newsletter pour deep-dives écrits adjacents
- Possibilité format Netflix/streaming si traction massive

## Métriques de succès

| Période | Cible vues moyenne | Cible subs | Cible AVD | Cible CTR |
|---------|--------------------|-----------|-----------|-----------|
| Sem 1-2 | 200-1000 | 30-150 | 8 min | 2.5% |
| Mois 1 | 2000-8000 | 300+ | 12 min | 4% |
| Mois 3 | 15000+ | 3000+ | 15 min | 6% |
| Mois 6 | 60000+ | 20000+ | 18+ min | 8%+ |

Note : C2 a les cibles vues les plus basses des 4 channels mais l'AVD absolue la plus haute. Watch time total = supérieur à C3 malgré moins de vues. L'algo récompense.

## Brief template

Structure obligatoire :
1. Hook + question centrale (30 sec) — pose la complexité d'entrée
2. Pourquoi ça compte maintenant (1 min) — actualité hook
3. Acte 1 (4-6 min) — état des lieux factuel
4. Acte 2 (6-8 min, 2-3 sous-sections) — complexification, angles divergents
5. Acte 3 (6-8 min) — points de tension, contradictions identifiées
6. Acte 4 (4-6 min) — convergence, ce qu'on apprend
7. Acte 5 (3-5 min) — ouverture, prospective, état des débats
8. Closing : sources principales en image + question ouverte (1 min)
9. CTA discret + Liens
10. Métadonnées (titre, chapters, description 800+, tags, pinned comment)
11. Critères qualité (sources primaires citées, multi-angles respectés, anti-slop)
12. Production estimée + temps swarm

## Patou-Overseer scan

- Voice quality check : voice_id != default
- Voice ≠ C1 Stillcraft voice (audience separation)
- Speaking rate compliance : 0.95-1.05
- SEO compliance : 8+ chapters + description 800+ mots + manual transcript + pinned comment sources
- Multi-angle compliance : minimum 4 angles documentés dans le brief reflétés dans le script
- AVD à 48h post-publish : si <50% du runtime → alerte (doc audience est exigeante)
- Cadence : 1 vidéo/semaine minimum
- D2 compliance : pas voix Pat, pas face Pat — channel anonyme verrouillé
