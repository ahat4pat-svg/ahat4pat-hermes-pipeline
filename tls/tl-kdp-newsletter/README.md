# TL KDP / Newsletter / Écriture

> Team Leader · Publication écrite (newsletter, KDP, éventuellement Substack)
> Reports to : Claude (Director)
> Audité par : Patou-Overseer (independent)

## Mission

Phase 2 mission incarnée — enseigner pour enlever de l'angoisse au monde — via :

- **Newsletter Décodeur IA en français** (lancement semaine du 10 juin)
- **KDP livres courts** — premier titre : *Comprenez Claude en 30 pages* (draft semaine 2)
- **Éventuellement Substack** (si newsletter prend, mirror sur Substack pour audience anglo)

## État actuel (2026-06-04)

- **3 sujets newsletter prêts** sur Desktop (`FEUILLE-NEWSLETTER-2026-06-04.html`) :
  1. L'idée est tout
  2. AI cite YouTube #1
  3. Coût 40¢ per vidéo
- **Workflow folders créés** : `~/Linux/newsletter/2026-06-04-jour/topic-{1,2,3}-*/`
- **Publer Pro re-souscrit** 2 juin ($16.56 CAD/mo) — couvre LinkedIn + X + Facebook + TikTok à venir
- **KDP** : titre verrouillé, draft à venir semaine 2

## Sous-agents Hermès

| Sous-agent | Rôle | Modèle |
|------------|------|--------|
| `newsletter-drafter` | Écrit drafts newsletter en voix Pat | DeepSeek V3.2 + voice-corpus Pat |
| `newsletter-correcteur` | Vérifie style + voice + image-first | Claude Sonnet |
| `newsletter-publisher` | Publie via Publer Pro (LinkedIn + X + FB + TikTok) | Publer API |
| `kdp-drafter` | Écrit chapitres KDP (format livre court) | DeepSeek V3.2 |
| `kdp-formatter` | Format Kindle KDP (epub/mobi) | Pandoc + scripts |

## Stack publication

| Outlet | Plateforme | État |
|--------|-----------|------|
| Newsletter | Publer Pro → LinkedIn + X + FB | $16.56/mo actif |
| KDP | Amazon KDP | gratuit, royalties 35-70% |
| Substack | (futur) | gratuit, mirror |

## Voice & style

Voice corpus Pat dans `~/.hermes/profiles/social/voice-corpus.md`. Règles clés :
- **Auto-implication PURE** : jamais pointer le lecteur, toujours « j'ai réalisé / j'ai vécu » + question ouverte
- **Image-First** : scène plantée AVANT pensée
- **Mise en situation** style Le Soleil, pas Journal de Québec
- **Influences** : Dostoïevski, Balzac

## Blockers

- Première newsletter à publier (semaine du 10 juin)
- Draft KDP « Comprenez Claude » à attaquer

## Prochaine milestone

- Newsletter #1 envoyée — semaine du 10 juin
- KDP draft complet — fin juin
- 100 abonnés newsletter — fin juin

## Sujets futurs en banque

- Le miroir IA — ce que notre comportement avec une IA révèle de nous
- La 3e personne (audit externe NotebookLM) — méthode pour penser hors de sa boucle

## Liens

- [Feuille Newsletter Desktop](../../../../../Desktop/FEUILLE-NEWSLETTER-2026-06-04.html)
- [Voice corpus](../../../../.hermes/profiles/social/voice-corpus.md)
- [ORG_CHART du repo principal](../../ORG_CHART.md)
- [memory.md](memory.md)
- [project.json](project.json)
