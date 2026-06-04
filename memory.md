# memory.md — Lexicon global AHat4Pat Hermès Pipeline

> Fichier de mémoire persistante partagée par tous les TLs et Hermès sub-agents.
> Mis à jour à chaque session de travail.

## Identité de l'organisation

- **Brand officiel** : AHat4Pat (A majuscule collé, AUtomations avec S — JAMAIS "A Hat 4 Pat" espacé)
- **CEO** : Pat (Patrick Lemieux) — ex-fondateur KAÏN, double-platine, ex-prof, indie hacker IA
- **Director** : Claude (Anthropic Opus 4.7)
- **Watchdog** : Patou-Overseer
- **Mission** : démocratiser la production IA québécoise authentique + revenu freelance + AI agents B2B

## Noms verrouillés (ne pas modifier sans Pat)

### Channels Faceless YouTube
- **C1 Stillcraft** — construction long-form, niche cottagecore + craft
- **C2 Loopkeeper** — ambient cinematic loops, niche midnight + atmospheric
- **C3 Stacklab** — AI Tutorials, niche indie hacker + automation
- **C4 Karmawatch** — micro-dramas verticaux 60 sec, niche noir suspense

### Produits / Plateformes
- **Juniors4Pat (J4P)** — AI Agents as a Service, 225 produits planifiés $19-79
- **Décodeur IA en français** — newsletter
- **Comprenez Claude en 30 pages** — premier KDP

### Personnes
- **Pat** = Patrick Lemieux (CEO)
- **Ju** = Julie de Drummondville (duo musical Pat et Ju, Lac-St-Jean été 2026)
- **Annie** = voix AI synthétique (Vapi/Twilio test +1 826 334 9040)

### Infrastructure
- **Beck** = Hetzner VPS 65.109.135.115 (root accès, OpenCode + Claude Code installés)
- **Billie** = OpenClaw dormant (archivé 18 avril 2026)
- **Paperclip VPS** = LiteLLM serveur 135.181.250.114

## Voix de Pat (template)

### Drew/Thinkverse AI style (FR-CA adapté)

Signatures à voler :
- "Lock in" → "Attache ta tuque" ou "Ferme tout le reste"
- "Watch this" → "Regarde ben ça"
- "Let me do the math live" → "On fait le calcul live"
- "Fair warning" → "Petit avertissement"
- "Real numbers, real receipts" → "Le vrai monde, les vrais chiffres"

Métaphores caricatures (à utiliser massivement) :
- Plutôt que Costco / DMV / Wells Fargo → SAAQ / urgence Sacré-Cœur / caissier Maxi dimanche soir / lave-auto Beauce
- Pattern : chaque concept abstrait = image matérielle québécoise reconnaissable

Ton :
- Conversationnel bar-style, comme ami sur le sofa
- Énergie haute mais pas criée
- Phrases courtes claquées + phrases longues qui déroulent
- Pause [music] programmée dans script = respiration

### Kit anglais (parallèle, moins classique)

Quand on fait du contenu en EN :
- Moins de "Sup guys" et "What's up everybody"
- Plus de phrases directes et observation québécoise (l'angle francophone qui regarde l'anglosphère)
- Garder les analogies caricatures mais switcher pour références US ou universelles

## Règles de production verrouillées

1. **JAMAIS ElevenLabs default voices** → algorithm YT throttle (slop detection)
2. **Voice clone Pat custom** OU voix réelle Pat enregistrée (NT1-A + Mackie + GarageBand) — choix par vidéo selon temps disponible
3. **Speaking rate ElevenLabs 0.9-1.2** strict (au-delà rétention chute)
4. **Vidéos C3 long-form 10-20 min** (94% des AI-cited videos)
5. **Chapters dans description OBLIGATOIRE** (78% des videos avec chapters sont citées multiple fois par AI)
6. **Description 500+ mots** avec brand names, lieux, concepts nommés
7. **Transcript manuel uploadé** via YT Studio (PAS YT auto-caption, trop d'erreurs)
8. **C4 vertical strict 1080×1920**
9. **Zero-padding scene_001.mp4** (anti sort alpha bug ffmpeg)
10. **ffmpeg flag `-shortest` IMPÉRATIF** (anti silence gênant)
11. **Lexique persistent Whisper** = règle "No Orphan" : noms propres "Stillcraft", "Loopkeeper", "Stacklab", "Karmawatch", "AHat4Pat", "Juniors4Pat", "L'", "C'"
12. **Burney style sous-titres karaoké** = mouvement sur mot actif

## Stratégie monétisation

### Court terme (0-90 jours)
- **Affiliate first** (Drew model) : PayKickstart ou ClickBank
- **C3 Stacklab** pousse Hermès SDK / Claude Code / Modal / outils cités dans nos briefs
- Bitly cleanup des liens

### Moyen terme (3-12 mois)
- **J4P AI Agents Sales** product launch lundi 9 juin
- **KDP first product** "Comprenez Claude en 30 pages" — draft sem 2 juin
- **Newsletter "Décodeur IA en français"** lancement sem 2 juin
- **Voice services international** post AI Agents launch
- Stack 8 streams Ali Abdaal modèle

## Décisions architecturales verrouillées (4 juin 2026)

1. **Claude = Director, pas executor** — délègue à Hermès via TLs
2. **Hermès Agent = front executor** — NousResearch framework, 140k stars GitHub
3. **Patou-Overseer = watchdog indépendant** — accès direct Pat, pas via Claude
4. **6 TLs identifiés** — un dossier par TL dans `tls/`
5. **n8n = orchestrateur production** — déjà en place chez Pat
6. **Modal GPU + Cloudflare R2** — infrastructure de base
7. **Coût cible** : ~0.40$/vidéo de 8 min (0.05$/min)

## À ne JAMAIS faire

- Mock des données critiques (règle CLAUDE.md #11 testée violation passée)
- Voice default ElevenLabs
- Publier sans chapters + description 500+ mots + transcript manuel
- Mettre AI avatars Pat (préférer son vraie voix ou voice clone)
- Toucher fenêtres ouvertes de Pat (osascript open/activate)
- Cat sur fichier avec secret (grep + masquage uniquement)
- Re-débattre l'org chart sans Pat
