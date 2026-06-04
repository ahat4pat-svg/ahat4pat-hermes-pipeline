# GarageBand Setup — Pat Voice Template (figé)

> Setup figé pour ré-enregistrer 1-2 mots à tout moment sans recalibrer.
> Charger ce template avant chaque session.

## Hardware

- **Mic** : Rode NT1-A (condensateur cardioïde)
- **Interface** : Mackie ProFXv3 (USB)
- **Shield** : Aokeo pop filter + reflection shield
- **Câble** : XLR Mackie → NT1-A
- **Headphones** : monitoring via Mackie out

## Template GarageBand à créer (1 fois, puis charger)

### Étape 1 — Nouveau projet
1. GarageBand → New Project → **Voice** template
2. Save As → `~/Music/GarageBand/AHat4Pat-Voice-Template.band`

### Étape 2 — Configuration entrée audio
1. GarageBand → Preferences → Audio/MIDI
2. **Input device** : Mackie ProFXv3
3. **Output device** : Mackie ProFXv3 (pour monitoring)
4. **Sample rate** : 48 kHz (compatible YouTube + ElevenLabs)
5. **I/O buffer size** : 64 (low latency monitoring)

### Étape 3 — Piste vocale
1. Add Track → Audio
2. **Input source** : Channel 1 Mono
3. **Format** : Mono input → Stereo output
4. Enable :
   - ✅ Monitoring (pour entendre ta voix dans tes phones)
   - ✅ Record Enable (rouge)
5. Track name : `Pat-Voice-Main`

### Étape 4 — Plugins audio (ordre critique)

Insère dans cet ordre sur la piste :

1. **Channel EQ** — preset "Voice Male Warm"
   - High-pass filter à 80 Hz (coupe rumble basse)
   - Boost léger 3 dB à 200 Hz (chaleur)
   - Cut 3 dB à 2 kHz (anti-stridence)
   - Boost 2 dB à 8 kHz (présence/air)

2. **Compressor** — preset "Vocal Compressor"
   - Ratio : 3:1
   - Threshold : -18 dB
   - Attack : 10 ms
   - Release : 100 ms
   - Make-up gain : +6 dB (auto)

3. **De-Esser** — preset par défaut
   - Frequency : 6 kHz
   - Threshold : -20 dB
   (atténue les "ssss" prononcés)

4. **Vocal Doubler** — DÉSACTIVÉ par défaut (activer seulement pour effets spéciaux)

5. **Reverb** — DÉSACTIVÉ par défaut (jamais reverb sur voice over YouTube, on l'ajoute en post si besoin)

### Étape 5 — Mackie réglages physiques

À régler UNE FOIS sur le Mackie ProFXv3 puis ne plus toucher :

- **Channel 1 (NT1-A)** :
  - Gain (knob du haut) : à **2 heures** (test : parle normalement, peak à -12dB max sur GarageBand)
  - +48V phantom power : **ON** (LED rouge allumée)
  - Low cut : **OUT** (on le gère dans GarageBand)
  - EQ knobs : **flat** (12h sur les 3)
  - Pan : **C** (center)
  - Aux 1/2 : **0**
  - Mute : **OFF**
- **Main Mix** : à **unity (0 dB)** (12h)
- **USB output** : level à 75%

### Étape 6 — Position mic (physical setup)

- NT1-A à **15-20 cm de la bouche** (largeur d'une main)
- Pop filter Aokeo entre toi et le mic, **3-5 cm devant le mic**
- Mic LÉGÈREMENT off-axis (ton souffle ne tape pas direct sur la capsule)
- Reflection shield Aokeo derrière le mic (atténue room reverb)
- Position : assis droit, mic à hauteur menton-bouche

### Étape 7 — Save template

1. File → Save As Template
2. Nom : `AHat4Pat Pat Voice Template`
3. Catégorie : Voice

Désormais : New Project → Pick template → tout est chargé.

## Workflow quotidien (post-setup)

### Pour enregistrer 1-2 mots (replacement)

1. Ouvre `AHat4Pat-Voice-Template.band`
2. Cmd+R : enregistre
3. Dis le mot
4. Cmd+R stop
5. Sélection → Export → Share → Export Song to Disk
6. Format : **WAV 48 kHz 24-bit**
7. Sauvegarde dans : `~/Linux/faceless-yt/pipeline/tls/tl-faceless-yt/voice-bank/replacements/YYYY-MM-DD-mot.wav`

### Pour enregistrer une session complète (vidéo entière)

1. Ouvre template
2. Cmd+N pour nouveau projet basé sur template
3. Enregistre par segments (1 paragraphe = 1 prise)
4. Comp les meilleures prises (selection → comp track)
5. Export WAV master
6. Output vers : `~/Linux/faceless-yt/pipeline/tls/tl-faceless-yt/channels/<c-channel>/assets/voice/<brief-id>-master.wav`

## Targets techniques (validation post-record)

- ✅ Pic max : -3 dB (jamais 0 dB = clip)
- ✅ Niveau moyen : -18 dB à -12 dB
- ✅ Bruit de fond : < -60 dB pendant silences
- ✅ Pas de plosives (p, b, t) qui font sauter le meter
- ✅ Pas de souffle bouche audible

## Si problème courant

| Problème | Solution |
|----------|----------|
| Bruit de fond constant | Augmente gain Mackie d'1 cran, baisse fader main |
| Voix trop "boxée" | Éloigne-toi du mic (proximity effect réduit) |
| Plosives qui sautent | Recule pop filter + parle légèrement off-axis |
| Crackle/distorsion | Phantom power +48V coupé, ré-allume |
| Pas de signal | Vérifie XLR bien clipé + channel 1 selected dans GarageBand |
| Latence monitoring | I/O buffer size : 32 ou 64 (pas 128+) |

## Pour ElevenLabs voice clone (30 sec sample)

Quand prêt :

1. Ouvre template
2. Enregistre 30 sec de toi parlant naturellement (un sujet que tu connais, conversationnel)
3. Export WAV 48 kHz 24-bit
4. Va sur elevenlabs.io → Voice Lab → Add Voice → Instant Voice Cloning
5. Upload le WAV
6. Nom : `pat_custom`
7. Save → copy le voice_id
8. Ajoute dans `.env` : `ELEVENLABS_VOICE_ID_PAT=<voice_id>`

Done. La voix Pat est clonée pour toujours, accessible via API.

## Notes

- Le template est PORTABLE : tu peux le copier sur un autre Mac, ça reload tout
- Si Mac mise à jour casse le template : re-créer en suivant les étapes
- Plugins listés sont tous DEFAULT GarageBand (pas d'achat nécessaire)
- Si tu veux upgrader plus tard : Logic Pro X = même logique, plus de plugins
