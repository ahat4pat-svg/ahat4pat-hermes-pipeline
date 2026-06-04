# C3 Brief 02 — « J'ai automatisé 100 vidéos YouTube pour 40$ avec Claude Code »

> Channel : C3 Stacklab · Workflow : Tutorial Educational Drew-style FR-CA · Durée cible : 10-12 min · Format : long-form horizontal 16:9

## Hook (first 7 sec)

> *« Quarante piastres. Pas par mois. Pas par semaine. Total. Pour CENT vidéos YouTube. Au complet. Voix, visuels, montage, le kit. Je l'ai fait, j'ai les reçus, pis dans les 10 prochaines minutes je te montre exactement comment. »*

## Pourquoi ça pop

- **Chiffre choc spécifique** ($40 / 100 vidéos = 40¢/vidéo)
- **Hook proof-driven** ("j'ai les reçus") = anti-bullshit posture Drew
- **Promesse claire** : recette complète en 10 min
- **Cadence québécoise** : "piastres" + "le kit" = signature FR-CA

## Promise / Stakes

> *« Petit avertissement : si t'as pas 12 minutes pour apprendre un système qui va te payer dès demain, ferme la vidéo. C'est pour le monde sérieux. Saute pas d'étape pis viens pas chialer dans les commentaires que ça marche pas. Ferme tout le reste. On y va. »*

## Plan 6 étapes

### Étape 1 — La math live (1 min)
Décompose le 40¢ en direct :
- Voix ElevenLabs : 0.01$/génération × 8 segments = 0.08$
- Image FLUX Schnell : 0.003$/megapixel × 5 images 1080p = 0.015$
- Clips LTX-2 : 0.23$/clip × 1 (le hero shot, le reste = stock) = 0.23$
- Modal GPU : 0.05$ pour la job complète
- **Total : ~0.40$**
- Compare au traditionnel : 2-4 semaines + équipe = facilement $500+

### Étape 2 — Le stack gratuit-pour-vrai (2 min)
- Google Flow + Nano Banana 2 (unlimited gratuit) pour images
- Meta AI ou Qwen (unlimited gratuit) pour vidéo clips simples
- Google AI Studio TTS (unlimited gratuit) pour voiceover backup
- Byte Plus Seedance 1.5 Pro (free credits avec audio inclus)
- **Total gratuit : 80% du pipeline**

### Étape 3 — Là où ça vaut payer (1.5 min)
- ElevenLabs voice clone (5$/mo) : ta voix unique = ton brand
- Higgs Field (30$/mo) : Seedance 2.0 pour les hero shots
- Modal GPU starter (30$/mo gratuit en crédit) : compute serverless
- **Total payant utile : ~10-30$/mo selon volume**

### Étape 4 — Le prompt qui change tout (3 min)
Démontre live : prompt Claude pour générer le script complet :
```
You are the GOAT script writer. Write me a 10-minute French-Canadian YouTube script on [TOPIC]. Hook in first 5 sec with information gap. Pattern interrupts every 60-90 sec. Conversational, no robot energy. Make it feel like I'm talking to a friend. End with strong CTA.
```
Pas générique. Pat-shape.

### Étape 5 — L'assemblage ffmpeg one-liner (2 min)
```bash
ffmpeg -i visuals.mp4 -i audio.wav -c copy -map 0:v -map 1:a -shortest output_final.mp4
```
Explique le flag `-shortest` (anti-silence). Démontre zero-padding `scene_001.mp4`.

### Étape 6 — Le piège dont personne parle (1.5 min)
**L'idée est tout.** 100 vidéos pour 40$ ne vaut RIEN si t'as 100 mauvaises idées. Recommande méthode manuelle Grant Owen (moving average top 20 % creators) — gratuite, 30 min/semaine.

## Closing FOMO (30 sec)

> *« Le monde qui va commencer la semaine prochaine, dans 6 mois ils se ramassent à 200 abonnés. Le monde qui commence ce soir, dans 6 mois ils impriment des vidéos en dormant. C'est pas dur de choisir. Le lien vers tout le stack dans la description. Lock in. On se r'voit dans la prochaine. »*

## CTA + Liens (description vidéo)

- Lien affiliate ElevenLabs (PayKickstart ou direct)
- Lien affiliate Higgs Field
- Lien Modal (no affiliate, juste référence)
- Lien Newsletter "Décodeur IA en français"
- Lien Juniors4Pat (waitlist AI Agents Sales)

## Métadonnées vidéo (pour SEO + AI citation Romayroh)

- **Titre A/B test** :
  - A : "J'ai automatisé 100 vidéos YouTube pour 40$ avec Claude Code"
  - B : "Le coût réel d'une vidéo YouTube IA en 2026 (j'ai les chiffres)"
- **Description 500+ mots** OBLIGATOIRE avec mention : Claude Code, Anthropic, ElevenLabs, FLUX Schnell, LTX-2, Modal, Google Flow, Nano Banana 2, Higgs Field, Byte Plus Seedance, Qwen, Meta AI, ffmpeg, n8n, faceless YouTube, AI video generation 2026, coût production vidéo
- **Chapters** (4-6 minimum) :
  - 00:00 - La math live (40¢ décortiqué)
  - 01:00 - Le stack gratuit
  - 03:00 - Là où ça vaut payer
  - 04:30 - Le prompt Claude qui change tout
  - 07:30 - Assemblage ffmpeg
  - 09:30 - Le piège : l'idée est tout
- **Tags** : claude code, faceless youtube 2026, ai video generation, automation video, hermes agent, free ai tools, low cost video, flux schnell, ltx-2
- **Transcript manuel uploadé** (PAS auto-caption)

## Visuels nécessaires

- Screen recordings : Claude Code CLI en action, Google Flow, ElevenLabs dashboard, ffmpeg terminal output
- B-roll : graphique coûts (Canva ou Remotion), table comparative trad vs IA
- Thumbnail : ton character Pat avec gros chiffre "40¢" en accent orange + sous-titre "100 VIDÉOS"

## Voice over

- Modèle : ElevenLabs `eleven_multilingual_v2`
- Voice ID : `pat_custom` (quand voice clone fait)
- Speaking rate : `1.1`
- Balises émotionnelles : `[ton sec]` pour les chiffres, `[léger sarcasme]` pour la partie "viens pas chialer"

## Critères qualité (anti-AI-slop)

- ✅ Au moins 5 métaphores québécoises (formulaire SAAQ, lave-auto Beauce, file Sacré-Cœur, etc.)
- ✅ Au moins 3 "signatures" Drew-style ("Lock in", "Petit avertissement", "On fait le calcul live")
- ✅ Voix réelle Pat OU voice clone Pat (PAS default ElevenLabs)
- ✅ Speaking rate 0.9-1.2
- ✅ Burney style sous-titres karaoké
- ✅ Chapters dans description
- ✅ Transcript manuel uploadé

## Production estimée

- Script + brief refining : 30 min (toi + moi)
- Voice recording : 15 min (toi)
- Visuals generation : 20 min (Hermès sub-agent automatique)
- Édit + sync : 30 min (Hermès sub-agent + ta validation)
- Upload + métadonnées : 15 min
- **Total : ~1h50 production · publication même jour**

## Status

🟡 **Brief prêt** · à exécuter quand pipeline + voix dispo
