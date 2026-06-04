# TL Voice Services International

> Team Leader · Services voix bilingue QC/EN (voice over, AI receptionists, voice clones)
> Reports to : Claude (Director)
> Audité par : Patou-Overseer (independent)

## Mission

Capitaliser sur la rareté de la voix bilingue QC/EN authentique pour offrir des services voice à l'international, particulièrement :

- **Voice over** (corporatif, publicité, narration FR-CA + EN)
- **AI receptionists** sectoriels (médical, dentaire, légal, immobilier QC)
- **Voice cloning** clients (avec consentement)
- **Voice agents** (commerce conversationnel)

Le marché QC n'est pas prêt pour AI receptionist (selon Pat). Le marché EN/US/global est mature et la voix bilingue Pat-style se vend bien.

## État actuel (2026-06-04)

- **Stack à installer cette semaine** — setup gratuit pour la plupart des composantes
- **ElevenLabs Pro** : déjà actif (compte Pat)
- **Vapi** : à brancher (free tier suffit pour démarrer)
- **Twilio** : à brancher (pay as you go)
- **Annie** : réceptionniste IA prototype · numéro +1 826 334 9040 · à tester live

## Sous-agents Hermès

| Sous-agent | Rôle | Modèle / Tech |
|------------|------|---------------|
| `voice-synth` | Synthèse voice ElevenLabs (avec FORBIDDEN_VOICES guard) | ElevenLabs API |
| `voice-clone-mgr` | Gère voice clones clients (consentement + storage) | ElevenLabs Voice Lab |
| `receptionist-router` | Route appels entrants → script approprié | Vapi + Twilio |
| `voice-agent-conv` | Voice agent conversationnel commerce | Vapi + OpenAI/Claude |

## Stack technique

| Couche | Tech | Coût |
|--------|------|------|
| TTS | ElevenLabs Pro | déjà actif |
| Voice cloning | ElevenLabs Voice Lab | inclus Pro |
| Telephony | Twilio + Vapi | pay as you go |
| Brain (conversation) | Claude/GPT via LiteLLM | inclus stack |
| Recording/QA | (à déterminer) | TBD |

## Blockers

- Setup Vapi (15-20 min)
- Setup Twilio (branchement) — Pat peut avoir déjà un compte
- Test Annie voices live au +1 826 334 9040

## Prochaine milestone

- Premier client voice over service (Phase 1 cash)
- Premier client AI receptionist (Phase 1.5)
- Voice clone client live (Phase 1.5)

## Liens

- [Annie test page](../../../../ops-control/ui/annie-test.html)
- [Architecture Annie](../../../../ops-control/ui/architecture-annie.html)
- [ORG_CHART du repo principal](../../ORG_CHART.md)
- [memory.md](memory.md)
- [project.json](project.json)
