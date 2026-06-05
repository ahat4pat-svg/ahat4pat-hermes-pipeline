# Claude Backup — Infrastructure de failover

> Préparé : 2026-06-04 (updated)
> État : **3 options préparées + setup minimal scripté**. Pat décide laquelle activer.
> Trigger failover : Claude principal silent > 5 min en milieu de tâche critique OU panne Anthropic API

## Pourquoi un backup

Si la session Claude principale tombe (Anthropic API down, problème réseau Mac, Claude Code crash, contexte saturé sans recovery), il faut une instance de secours qui :
- Peut reprendre la conversation avec Pat sans perdre la mémoire système
- Peut continuer le travail en cours (orchestration TLs, lecture mémoire, exécution skills)
- Peut alerter Pat que le principal est down (via Patou-Overseer)

**Pas une réplique exacte** — un secours qui sait où sont les choses et peut continuer.

## Les 3 options préparées

### Option A — Beck VPS (Hetzner)

**Setup existant** :
- Beck = ubuntu-8gb-hel1-1 chez Hetzner, accessible `ssh root@65.109.135.115`
- OpenCode 1.4.0 déjà installé
- Config LiteLLM déjà présente `/root/.config/opencode/config.json` pointant vers `http://135.181.250.114:4000/v1`
- Claude Code (`@anthropic-ai/claude-code`) installé

**Étapes activation (~15 min)** :
1. SSH dans Beck : `ssh root@65.109.135.115`
2. Sync memory (cron 5 min) : voir Setup minimal ci-dessous
3. Sync repo Hermes : `git clone https://github.com/ahat4pat-svg/ahat4pat-hermes-pipeline.git /root/hermes-pipeline`
4. Démarrer Claude Code sur Beck avec contexte Pat : `claude --memory-dir /root/.claude/memory`
5. Configurer Telegram bot relay : Patou-Overseer alerte « Claude principal down, Beck Claude actif »

**Avantages** :
- Tu es sur Beck = même infra que CTO agent, déjà relié au stack
- LiteLLM chain déjà active, peut router vers Claude Opus 4.7 via OpenRouter
- Coût : déjà payé (Beck $5/mo running)
- Pat peut SSH dans Beck depuis n'importe quel device

**Inconvénients** :
- Latence + complexité SSH (Pat doit ouvrir terminal SSH)
- Pas d'interface conversationnelle directe — c'est une session CLI sur VPS distant
- Si Beck tombe, double-down (mais ça arrive moins souvent qu'Anthropic API)

### Option B — Nous Portal Plus

**Setup existant** :
- Compte Nous Portal Plus actif ($20/mo) — `ahat4pat@gmail.com`
- Hermes-4-70B + 4 tools (Browser Use, FAL, OpenAI TTS, Firecrawl)
- Web interface accessible depuis n'importe quel browser

**Étapes activation (~5 min)** :
1. Pat va sur portal.nousresearch.com (déjà loggé)
2. Démarre une nouvelle session avec un system prompt « tu es Claude backup pour Pat »
3. Upload mémoire système comme fichiers attachés à la conversation (ou colle MEMORY.md inline)
4. Reprend la conversation

**Avantages** :
- ZÉRO config supplémentaire, déjà payé, déjà setup
- Interface web simple = Pat peut accéder de mobile, autre Mac, n'importe où
- Hermes-4-70B est compétent (utilisé déjà pour Pup + Patou)
- Tools (Browser Use, Firecrawl) disponibles pour actions

**Inconvénients** :
- Pas Claude — Hermes-4-70B (différent style, différentes forces)
- Pas de continuité mémoire automatique — Pat doit copier-coller ou attacher la mémoire à chaque session
- Modèle plus petit (70B vs Claude Opus 4.7) = moins de nuance dans le raisonnement

### Option C — LiteLLM chain direct

**Setup existant** :
- LiteLLM v1.83 déjà tourne sur Paperclip VPS `http://135.181.250.114:4000`
- 11 modèles disponibles incluant `ceo-think` (Qwen3-235B), `ceo-fast` (Llama4 Maverick 1M), `cto` (DeepSeek R1)
- Context fallbacks configurés : `ceo-think → ceo-fast`, `cto → ceo-fast`

**Étapes activation (~10 min)** :
1. Pat ouvre un client local (Claude Desktop OU Chatbox OU TypingMind OU equivalent)
2. Configure endpoint : `http://135.181.250.114:4000/v1`
3. Sélectionne `ceo-think` ou `ceo-fast` selon besoin
4. Démarre conversation avec system prompt mémoire chargée

**Avantages** :
- Modèles puissants (Qwen3-235B, Llama4 Maverick 1M context)
- Latence très basse (proxy direct)
- Coût : amorti dans le run rate existant
- Choix de modèle selon use case

**Inconvénients** :
- Plus de friction côté client (Pat doit installer/configurer un client)
- Pas un agent persistant — chaque session repart de zéro
- Pas Claude — modèles différents, comportements différents

---

## Recommandation Claude (pour Pat de décider)

**Option B (Nous Portal Plus)** est la plus économique en effort pour Pat :
- Déjà payée
- Web interface, accès partout
- Zero config supplémentaire
- Tools disponibles pour vrai travail (browser, scraping)

**MAIS** : si tu veux un VRAI failover automatique qui prend la relève sans intervention humaine, c'est **Option A (Beck)** :
- On peut configurer un health-check Patou qui détecte Claude principal down
- Patou démarre Claude sur Beck automatiquement
- Patou alerte Pat « tu peux SSH Beck maintenant, ton Claude est rendu là »

**Option C** : utile comme outil ad hoc (modèles puissants à la demande), pas un vrai backup conversationnel.

## Décision Pat — questions à clarifier

1. **Quel niveau d'automatisation** veux-tu ?
   - 100% manuel (Pat décide quand activer) → **Option B (Nous Portal)**
   - Semi-auto (Patou détecte + alerte + Pat active) → **Option A (Beck)** avec scripts SSH
   - Full-auto (Patou détecte + active + Pat reçoit notification) → **Option A** avec orchestration

2. **Importance de la continuité Claude-style** ?
   - Essentielle (réponses must feel like Claude) → **Option A** (Claude Code sur Beck)
   - Souhaitable mais pas critique (un autre LLM compétent OK) → **Option B** (Hermes-4-70B)
   - Pas important (juste besoin de continuer le travail) → **Option C** (modèle ad hoc)

3. **Budget supplémentaire** acceptable ?
   - $0/mo (utiliser ce qui est déjà payé) → **A ou B**
   - $20-50/mo (ajouter un service dédié) → variations possibles
   - $100+/mo (full redundance) → setup complet avec health monitoring

## Setup minimal (peu importe l'option choisie)

Indépendamment de l'option, ces 3 préparations doivent être faites :

### 1. Sync automatique mémoire système

```bash
# Cron toutes les 5 min — sync memory vers backup local + Beck si Option A
# À mettre dans crontab Mac de Pat (crontab -e)

*/5 * * * * /bin/bash -c '\
  rsync -av --delete \
    ~/.claude/projects/-Users-patrick-lemieux2outlook-com-Desktop-Linux/memory/ \
    ~/Documents/CLAUDE_MEMORY_BACKUP/ \
  && (if [ -f ~/.claude_backup_option_A ]; then \
       rsync -av ~/Documents/CLAUDE_MEMORY_BACKUP/ root@65.109.135.115:/root/.claude/memory/; \
     fi)'
```

Si Pat choisit Option A : `touch ~/.claude_backup_option_A` pour activer le sync vers Beck.

### 2. Patou-Overseer health check Claude principal

À ajouter au scan Patou existant (`~/Documents/Patou-Vault/patou_overseer.py` ou équivalent) :

```python
def check_claude_principal_alive():
    """Returns True if Claude principal a répondu dans les 30 dernières min pendant heures actives Pat."""
    last_activity_file = Path.home() / ".claude/projects/-Users-patrick-lemieux2outlook-com-Desktop-Linux/last_response.txt"
    if not last_activity_file.exists():
        return None  # Inconclusive
    last_mtime = datetime.fromtimestamp(last_activity_file.stat().st_mtime)
    now = datetime.now()
    # Pendant heures Pat actives (8h-23h)
    if 8 <= now.hour <= 23:
        return (now - last_mtime) < timedelta(minutes=30)
    return True  # Hors heures Pat, peu importe
```

Si fail X minutes : Patou notifie Pat par Telegram avec :
- « Claude principal silent depuis X min »
- « Option backup recommandée selon contexte : A / B / C »
- Lien direct vers Nous Portal OU commande SSH Beck OU client LiteLLM

### 3. RESUME-HERE-CLAUDE-[date].md updated proactively

Convention déjà en place : Pat update `~/Desktop/RESUME-HERE-CLAUDE-[date].md` à chaque milestone, pas juste compaction. Backup Claude charge ce fichier en premier pour récupérer l'état.

**Une convention secondaire à ajouter** : un script qui auto-export les derniers 200 tours de conversation Claude Code dans `~/Desktop/CLAUDE-LAST-CONVERSATION.md` toutes les 30 min. Ainsi le backup peut reprendre EXACTEMENT là où on était.

---

## Décision attendue Pat

**Une seule question** : A, B, ou C ?

- A = Beck VPS Claude Code (failover technique max, friction SSH)
- B = Nous Portal Plus Hermes-4-70B (zéro setup, web interface) ← recommandé pour ce soir
- C = LiteLLM chain (outils puissants ad hoc, pas vrai backup conversationnel)

Dès que tu choisis, je peux scripter le setup complet en < 30 min :
- Option A : crontab + sync Beck + Patou health check
- Option B : doc « comment activer en 5 min en cas de panne » + URL bookmark
- Option C : config client local + system prompt template

---

## Note Pat 4 juin

Pat a précisé ce soir : « comme tu sais, d'ici là, on a besoin d'avoir un backup. Fais-moi préparer ça. » → c'est ce document. Prêt à activer dès choix.
