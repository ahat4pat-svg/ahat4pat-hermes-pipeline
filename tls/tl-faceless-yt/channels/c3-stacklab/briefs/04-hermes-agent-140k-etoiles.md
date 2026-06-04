# C3 Brief 04 — « Hermès Agent : 140 000 étoiles GitHub en 3 mois. Le framework que personne n'a vu venir. »

> Channel : C3 Stacklab · 12-15 min · long-form 16:9

## Hook (7 sec)
> *« Cent quarante mille étoiles GitHub. En trois mois. Tu sais c'est quoi le projet de cette ampleur-là ? C'est Hermès Agent, par NousResearch, sous licence MIT. C'est gratuit. C'est souverain. Et 99% du monde sur YouTube ne te le mentionne PAS. Pourquoi ? Parce qu'il les rend obsolètes. »*

## Promise / Stakes
> *« Petit avertissement : si t'es solo creator ou indie hacker, ce que je vais te montrer dans les 12 minutes qui suivent va changer comment tu déploies des agents IA pour ta business. Pour toujours. Sans abonnement. Sans dépendance. Ferme tout le reste. »*

## Plan 5 sections

### Section 1 — Pourquoi 140k étoiles si vite (2 min)
- Le bon timing : Anthropic/OpenAI/Google rendent leurs SDK plus opaques → demande pour open-source explose
- Hermès propose : composition d'agents, function-calling JSON typé, mémoire multi-couches (FTS5 + résumés LLM persistants)
- vs OpenClaw : boucle séquentielle simple → Hermès = topologie Swarm (agents parallèles)
- Démontre : la table comparative (NotebookLM slide)

### Section 2 — Le concept clé : Skills auto-générés (2.5 min)
- Hermès crée AUTOMATIQUEMENT des skills (fichiers markdown) après chaque tâche complexe
- Métaphore : « C'est comme un employé qui prend des notes sur comment il a fait son job, puis ces notes deviennent un manuel que les autres employés utilisent »
- vs OpenClaw : compétences manuelles uniquement
- Long-term : Hermès devient plus compétent à chaque tâche sans intervention humaine

### Section 3 — Stack qu'on bâtit autour (2.5 min)
- Hermès Agent = orchestrateur (le cerveau délégué)
- Claude Code = CLI interface (le pilote)
- Modal GPU = compute serverless ($30/mo Starter free credit)
- ElevenLabs ou Qwen3-TTS = voice
- FLUX.2 + LTX-2 + Seedance = image-to-video
- n8n = production trigger/distribution
- Démontre : architecture diagramme

### Section 4 — Démo live : agent qui fait une vidéo en autonomie (3 min)
- Show terminal :
  ```bash
  claude 'Génère une vidéo C3 sur le sujet [TOPIC] en utilisant le brief dans tls/tl-faceless-yt/channels/c3-stacklab/briefs/'
  ```
- Hermès orchestre : Scénariste écrit → Audio synthétise → Visuel génère → Éditeur assemble
- Pendant ce temps : Pat continue à parler de la philosophie
- Reveal le MP4 final à la fin

### Section 5 — Comment commencer ce soir (2 min)
- Clone le SDK : `git clone https://github.com/mz2/hermes-agent-sdk.git`
- Install : `npm install -g @anthropic-ai/claude-code`
- Setup Modal : `modal setup`
- Lance ton 1er agent : `hermes init`
- Total setup : ~20 min

### Bonus — Pourquoi c'est éthiquement important (1.5 min)
- MIT = ton agent ne peut JAMAIS être pris en otage par un changement de pricing
- Souverain = tes données restent chez toi (vs Anthropic qui peut update ses ToS demain)
- Démocratique = quelqu'un avec 30$/mo a accès au même stack qu'une startup à 1M$ funding
- Tie back to mission : « Quand t'as zéro retraite et 100k de dettes, t'as pas besoin d'un autre abonnement. T'as besoin d'OUTILS qui te servent toi. »

## Closing FOMO (30 sec)
> *« Cent quarante mille devs l'ont déjà adopté. Dans 6 mois ce sera un million. Tu peux être early ou tu peux être en retard. Lien repo dans la description. Lock in. »*

## Affiliate angle
- Modal référence directe (pas affiliate yet, juste référence honnête)
- ElevenLabs affiliate link (PayKickstart ou direct)
- Higgs Field affiliate (Seedance 2.0)

## Métadonnées
- **Chapters** : 6 chapitres mappés sur les sections
- **Description 500+ mots** avec : Hermès Agent, NousResearch, MIT license, OpenClaw, Anthropic Claude Code, Modal GPU, ElevenLabs, Qwen3-TTS, FLUX.2, LTX-2, Seedance, n8n, Cloudflare R2, HyperFrames, Remotion, faceless YouTube, AI agents, function calling, JSON typed, Swarm topology, FTS5 SQLite, persistent memory
- **Tags** : hermes agent, ai agents 2026, claude code, faceless youtube ai, open source ai, nousresearch, modal gpu, indie hacker stack

## Production : ~2h
