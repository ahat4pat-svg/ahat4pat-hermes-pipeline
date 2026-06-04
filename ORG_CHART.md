# ORG CHART — AHat4Pat Hermès Pipeline

> Verrouillé le 4 juin 2026 par Pat. Ne PAS modifier sans Pat.

## Schéma (corrigé 4 juin avec Claude Backup + flèche Patou→Claude explicite)

```
                         Pat (CEO + Founder)
                               │
            ┌──────────────────┼──────────────────┐
            │                  │                  │
   Claude (Director) ◄────── Patou-Overseer ◄──── (alerte directe Pat si Claude OU TL dérive)
   = orchestration            (Watchdog)
            │                  │
   ┌────────┼────────┐         │
   │        │        │         │
   TLs (6) ◄────────────────── surveillés DIRECT par Patou
   │
   ├─ TL Faceless YT (4 channels C1-C4)
   ├─ TL Juniors4Pat
   ├─ TL Freelance
   ├─ TL Voice Services International
   ├─ TL KDP / Newsletter / Écriture
   └─ TL Musique (Pat, perso)

   Claude Backup ◄── ready to failover si Claude principal down
      └── all memory + briefs + repo state synchronisé
```

## Rôles et responsabilités

### Pat (CEO + Founder)

- Décisions stratégiques irréversibles
- Validation finale avant publication / livraison client
- Décisions financières (budget API, choix de plateformes)
- Interlocuteur final si Patou alerte dérive

### Claude (Director / Centre de Travail)

- Interlocuteur conversationnel UNIQUE de Pat
- Orchestre la communication entre les 6 TLs
- Rédige les briefs production
- Délègue exécution à Hermès via les TLs
- N'EXÉCUTE PAS le heavy lift lui-même (sauf demande explicite Pat)
- Supervise mais n'audite pas les TLs (c'est le rôle de Patou)

### Patou-Overseer (Watchdog)

- Scan **7 sources** : Claude + 6 TLs
- 2× par jour : 9h et 20h
- Alerte Telegram à Pat DIRECTEMENT si dérive (pas via Claude)
- Journal complet dans `~/Documents/Patou-Vault/`
- Mode `DRY_RUN=1` par défaut, `0` quand validé
- Ne PRENDS PAS de décisions, observe et alerte uniquement

### TLs (Team Leaders) — 6 départements

| TL | Domaine | Hermès sub-agent | Channels / Outputs |
|----|---------|------------------|---------------------|
| TL Faceless YT | 4 channels YouTube | drafter + producer | Stillcraft (C1) + Loopkeeper (C2) + Stacklab (C3) + Karmawatch (C4) |
| TL Juniors4Pat | AI Agents Sales B2B | waitlist + outreach + delivery | Réceptionniste IA + agents sectoriels |
| TL Freelance | Team A IMAP + Team B PME | scout + drafter + follow-up | Drafts Upwork + outreach PME QC |
| TL Voice Services International | Bilingue QC/EN voice | ElevenLabs + Vapi + Twilio | Voice over services + AI receptionists |
| TL KDP / Newsletter / Écriture | Publication écrite | drafter + correcteur + publish | Newsletter "Décodeur IA en FR" + KDP "Comprenez Claude en 30 pages" |
| TL Musique | Pat (perso, solo) | (à définir) | Cours guitare, sessions solo. ⚠️ Julie removed 4 juin — fini avec Julie. |

Chaque TL :
- Possède son propre `tls/<tl-name>/memory.md` (lexicon, décisions verrouillées)
- Possède son propre `tls/<tl-name>/project.json` (asset status, work history)
- Possède ses propres `tls/<tl-name>/skills/` (Hermès skills typés)
- Reporte à Claude pour orchestration
- Est audité par Patou indépendamment

## Principes accountability

1. **Patou peut alerter Pat directement si Claude dérive** — pas de boucle fermée
2. **Patou peut alerter Pat directement si un TL dérive** — sans filtre Claude
3. **Si divergence Claude ↔ TL** → arbitrage Pat sans tiers
4. **Aucun single point of failure** dans l'accountability

## Flux d'information typique

### Quand Pat demande quelque chose

```
Pat → Claude : "Je veux publier une vidéo C3 cette semaine"
Claude → réfléchit + propose plan + écrit brief
Claude → TL Faceless YT (sub-agent C3) : "Voici le brief, exécute"
TL Faceless YT → Hermès sub-agent : script + voice + visuals + render + upload
Patou observe : Pat alerté si écart > seuil
Pat reçoit : MP4 final + lien YouTube
```

### Quand un TL dérive

```
Patou détecte dérive (9h ou 20h scan)
Patou → Pat directement (Telegram bot Patou)
Pat décide : intervient + corrige
Claude apprend de la décision Pat (via mise à jour memory.md)
```

### Quand Claude dérive

```
Patou détecte incohérence Claude (memory contradicte org chart, ou exécute au lieu de déléguer)
Patou → Pat directement
Pat → Claude : "tu micro-manages, remonte au rôle director"
Claude met à jour comportement
```

## Stack technique par couche

| Couche | Tech |
|--------|------|
| Pat | Humain |
| Claude | Anthropic Claude Opus 4.7 (cette instance) |
| Patou | Python wrapper + Hermes-4-70B via OpenRouter |
| TLs | Hermès Agent (NousResearch framework) sub-agents |
| Hermès sub-agents | NousResearch Hermès Agent + skills custom + Modal GPU |

## Modification de cet org chart

Ce document peut être modifié UNIQUEMENT par Pat. Toute proposition de modification doit être discutée avec Pat avant édition. La date "verrouillé 4 juin 2026" doit être mise à jour si modification approuvée.
