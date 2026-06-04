# Workflow C3 Stacklab — Tutorial Educational Drew-style FR-CA

> Channel : C3 Stacklab · format long-form 10-12 min horizontal 16:9
> Voix : Pat réelle OU voice clone `pat_custom`
> Production cible : 2 vidéos/semaine (lundi + jeudi)

## Concept

Tutoriels AI / automation / indie hacker en français québécois, ton Drew/Thinkverse AI adapté FR-CA. Chaque vidéo = un playbook actionnable + outils cités + métaphores québécoises caricaturales.

## Stack technique

| Étape | Tool | Note |
|-------|------|------|
| Script | Claude Opus 4.7 | Prompt verbatim dans memory.md |
| Voice | ElevenLabs `eleven_multilingual_v2` voice_id `pat_custom` | Speaking rate 1.0-1.1 |
| Visuels | Screen recordings réels + B-roll Flux Schnell + scènes Seedance via Higgs Field | 80% screen, 20% B-roll |
| Édition | CapCut OR Remotion | CapCut pour démarrer, Remotion pour scale |
| Sous-titres | Whisper transcription → Burney style karaoké | mot actif accent orange |
| Stitch | ffmpeg `-shortest` | flag impératif |

## Pipeline Hermès

```
1. Brief MD validé Pat
   ↓
2. c3-drew-writer (Hermès skill)
   ├─ analyse competitor top 20% (méthode Grant Owen)
   ├─ génère script 1200-1500 mots Drew-style FR-CA
   └─ inclut chapters + description 500+ mots + tags
   ↓
3. generate_voiceover (Hermès tool)
   ├─ voice_id pat_custom
   ├─ speaking_rate 1.05
   └─ balises émotionnelles inline
   ↓
4. fetch_stock_assets + render_scene (parallel via Fork and Run)
   ├─ B-roll Pexels (5 assets)
   ├─ 2-3 scènes Seedance hero shots
   └─ Screen recordings : Pat enregistre OBS local
   ↓
5. stitch_video (Hermès tool)
   ├─ concat clips zero-padded
   ├─ overlay voice + music subtle
   └─ output MP4 H.264 1080p
   ↓
6. youtube-uploader (Hermès skill)
   ├─ upload via YouTube Data API
   ├─ ajoute chapters dans description
   ├─ upload transcript manuel (PAS auto-caption)
   ├─ schedule publication OR publish immédiat
   └─ ping Patou-Overseer pour audit post-publish
```

## Voice Pat — règles de production

### Signatures FR-CA à utiliser (au moins 3 par vidéo)
- "Lock in" → "Attache ta tuque" ou "Ferme tout le reste"
- "Watch this" → "Regarde ben ça"
- "Let me do the math live" → "On fait le calcul live"
- "Fair warning" → "Petit avertissement"
- "Real numbers, real receipts" → "Le vrai monde, les vrais chiffres"
- "Don't be that person who'll start next month" → "Sois pas le cousin qui dit y va commencer la semaine prochaine"

### Métaphores caricatures (au moins 5 par vidéo)
Liste utilisable (cycler) :
- Formulaire SAAQ
- File urgence Sacré-Cœur
- Caissier Maxi du dimanche soir
- Lave-auto de la Beauce
- Tim Hortons 6h du matin lundi
- Costco un samedi avec ta belle-mère
- Embouteillage pont Champlain
- Réception STM tableau jaune
- Bell technicien fenêtre 8h-12h
- Promesses de campagne municipale
- Permis construction Drummondville

### Énergie
- Haute mais pas criée
- Phrases courtes claquées + phrases longues qui déroulent
- Pauses respirées entre paragraphes (3 sec)
- Speaking rate 1.05 = standard, 1.1 si plus vif

## SEO / GEO (règles Romayroh strictes)

- **Long-form 10-20 min** (sweet spot 12 min)
- **Chapters dans description** : minimum 5, 1 par section
- **Description 500+ mots** avec entités nommées (Claude, Anthropic, Modal, ElevenLabs, etc.)
- **Transcript manuel uploadé** via YT Studio (PAS auto-caption — règle absolue)
- **Tags** : ai tools 2026, faceless youtube fr, claude code, automation québec, indie hacker, [topic-specific]
- **Title A/B** : préparer 2 titres et alterner

## Monétisation

### Phase 1 (0-1000 subs)
- Affiliate links dans description (PayKickstart OR ClickBank)
- Mentions naturelles d'outils dans le script (Hermès SDK, ElevenLabs, Modal, etc.)
- Bitly cleanup des URLs

### Phase 2 (1000+ subs + 4000 watch hours)
- YouTube Partner Program activé
- AdSense classique (revenue $/CPM en plus)
- Sponsors selon catégorie (SaaS, tools)

### Phase 3 (10k+ subs)
- Cours payant "Faceless YouTube québécois — le système complet" (modèle Ali Abdaal PTYA)
- Newsletter premium tier

## Métriques de succès

| Période | Cible vues moyenne | Cible subs | Cible AVD | Cible CTR |
|---------|--------------------|-----------|-----------|-----------|
| Sem 1-2 | 500-2000 | 100-300 | 4 min | 4% |
| Mois 1 | 5000-15000 | 1000+ | 5 min | 6% |
| Mois 3 | 30000+ | 10000+ | 6 min | 8% |
| Mois 6 | 100000+ | 50000+ | 7 min | 10%+ |

## Brief template (référence : 01 à 05 dans channels/c3-stacklab/briefs/)

Structure obligatoire :
1. Hook (7 sec) avec information gap
2. Promise / Stakes (10 sec)
3. Plan 4-6 sections (1.5-2 min par section)
4. Bonus / nuance éthique (1 min) — pas obligatoire mais souvent utile
5. Closing FOMO (30 sec)
6. CTA + Liens
7. Métadonnées (titre, chapters, description 500+ mots, tags)
8. Critères qualité (vérification anti-slop)
9. Production estimée

## Patou-Overseer scan

- Voice quality check : voice_id == pat_custom (pas default)
- Speaking rate compliance : 0.9-1.2
- SEO compliance : chapters + description 500+ mots + manual transcript
- Brief vs published : major deviation = alerte
- Cadence : 2 vidéos/semaine (alerte si saute)
