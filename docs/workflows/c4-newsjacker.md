# Workflow C4 Karmawatch — News-Jacker Shorts Verticaux

> Channel : C4 Karmawatch · format short 60 sec vertical 1080×1920
> Voix : Pat OR narrator anonyme noir style
> Production cible : 1 short/jour pendant 5 jours (semaine inaugurale)

## Concept

Micro-dramas noirs de 60 secondes. Twist par histoire. Thème central : dystopie IA quotidienne (extrapolations légères de ce qui existe déjà, jamais magie tech surnaturelle).

## Stack technique

| Étape | Tool | Note |
|-------|------|------|
| Script | Claude Opus 4.7 | Format JSON Hook-Body-CTA |
| Voice | ElevenLabs OR Qwen3-TTS | Speaking rate 0.9-0.95 (lent suspense) |
| Visuels | Seedance 2.0 via Higgs Field (hero) + FLUX Schnell (statiques) | Style noir grain blue-orange |
| Édition | HyperFrames OR Remotion | Burney karaoké subtitles |
| Sound | YouTube Audio Library + SFX library | Drone bass + SFX précis |
| Stitch | ffmpeg vertical 1080×1920 `-shortest` | Zero-padding scene_001.mp4 |

## Pipeline Hermès

```
1. Brief MD validé Pat
   ↓
2. c4-news-jacker (Hermès skill)
   ├─ découpe story en 8 scènes ~7-8 sec
   ├─ génère JSON SceneDefinition par scène
   └─ écrit voix narration ~120 mots (2.5 mots/sec × 60 sec)
   ↓
3. generate_voiceover
   ├─ speaking_rate 0.9 (lent suspense)
   ├─ balises [whisper] sur lignes choc
   └─ output WAV master
   ↓
4. render_scene (parallel via Fork and Run, 8 scènes)
   ├─ Seedance 2.0 pour scènes hero (3-4 sur 8)
   ├─ FLUX Schnell pour scènes statiques (4-5 sur 8)
   ├─ aspect_ratio "9:16" strict
   └─ duration_seconds 7-8 par scène
   ↓
5. stitch_video
   ├─ concat zero-padded scene_001 → scene_008
   ├─ overlay voice + drone bass low-volume
   ├─ Burney karaoké sous-titres (mot actif orange #d97706)
   └─ output MP4 vertical 1080×1920
   ↓
6. youtube-uploader
   ├─ upload comme YouTube Short
   ├─ description 300+ mots (oui même sur shorts pour AI citation)
   ├─ transcript manuel
   └─ ping Patou
```

## Règles de production verrouillées

### Format
- **Strict 1080×1920** vertical
- **Strict 60 sec MAX** (YT short cutoff)
- **Zero-padding** scene_001.mp4 obligatoire
- **No mid-roll ads** (impossible sur shorts)

### Sound
- **2.5 mots/seconde max** (au-delà = désync)
- **Drone bass continu** pour ambiance noire
- **Silence final 2-3 sec** pour impact twist

### Visuels
- **Style noir grain** : low-key lighting, blue-orange tint
- **Pas de visages identifiables** (anonymat + RGPD)
- **Asset Tokenization** : si série, garder même palette + style
- **Burney karaoké** : mot actif orange/jaune sur fond noir transparent
- **Sous-titres position** : center vertical (PAS bas — TikTok algo cache bas)

### Voice
- **Speaking rate 0.9-0.95** (lent suspense)
- **Balises émotionnelles** : `[whisper]` lignes choc, `[ton sec]` factuel, `[ton plat]` ironie
- **Voice Pat OR narrator anonyme** selon vibe drame

## Structure narrative obligatoire (60 sec)

| Scène | Durée | Fonction |
|-------|-------|----------|
| 1 | 0-3s | Hook frappant, première frame retient |
| 2 | 3-10s | Setup contexte |
| 3 | 10-22s | Mise en place mystère/conflit |
| 4 | 22-32s | Approfondissement |
| 5 | 32-45s | Twist révélation |
| 6 | 45-55s | Conséquence/implication |
| 7 | 55-58s | Punchline finale |
| 8 | 58-60s | Karmawatch logo + silence |

## Métadonnées

- **Titre** : punchy 50 char max (le hook ou la promesse)
- **Description 300+ mots** OBLIGATOIRE même sur shorts (règle Romayroh + AI citation)
- **Pas de chapters** (short = N/A)
- **Tags** : micro-drama, suspense court, twist video, vertical shorts, faceless storytelling FR, AI ethics, [thematic tags]
- **Transcript manuel** obligatoire (même sur shorts)

## Production estimée

- Script + brief refining : 15 min
- Voice (60 sec) : 10 min
- Visuels génération parallel : 20 min via Fork and Run
- Édit + vertical sync : 25 min
- Upload + métadonnées : 10 min
- **Total : ~1h20 par short**
- **5 shorts/semaine cible = ~7h/sem**

## Métriques de succès

| Période | Cible vues | Cible subs |
|---------|------------|-----------|
| Sem 1 (5 shorts) | 10k-50k views combinés | 100-500 |
| Mois 1 (20 shorts) | 100k-500k views | 1k-5k |
| Mois 3 (60+ shorts) | 1M+ views | 10k+ |

## Cross-pollination avec autres TLs

- **TL Faceless YT C3 Stacklab** : un short C4 peut teaser un long-form C3 du même thème
- **TL J4P** : si un drame illustre un cas d'usage AI Agents Sales = lead pour J4P
- **TL KDP Newsletter** : un short qui pop = sujet potentiel newsletter

## Patou-Overseer scan

- Speaking rate compliance : 0.9-1.0 (strict C4)
- Aspect ratio : 9:16 strict
- Duration : ≤60s
- Transcript manuel uploadé : oui
- Asset tokenization cohérence (si série thématique)
