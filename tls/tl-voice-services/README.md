# TL Voice Services International

> Team Leader · Services voix bilingue QC/EN
> Reports to : Claude (Director)
> Audité par : Patou-Overseer (independent)
> **État : équipe préparée 4 juin 2026 — prête à activer dès API keys**

## Mission

Capitaliser sur la rareté de la voix bilingue QC/EN authentique pour offrir des services voix à l'international, particulièrement :

- **AI receptionists** sectoriels (médical, dentaire, légal, immobilier QC) — Phase 1 cash recurring
- **Voice over** (corporatif, publicité, narration FR-CA + EN) — Phase 1 cash one-shot
- **Voice cloning** clients (avec consentement écrit) — Phase 1.5 différenciateur
- **Voice agents** (commerce conversationnel, sales outbound) — Phase 2 expansion

Le marché QC est mûr pour AI receptionists (PME services de santé/légal/immobilier). Le marché EN/US/global est mature pour voice over + voice cloning. **TL Voice = production / TL J4P = vente** (voir `CROSS-LINK-J4P.md`).

## État (2026-06-04)

✅ **Préparé ce soir** :
- Architecture complète documentée
- Vapi config base prête (`vapi-config/receptionist-base.json`)
- 4 scripts secteurs détaillés (médical, dentaire, légal, immobilier)
- Pricing structure 3 tiers + voice over + cloning (`pricing/structure-2026-06.md`)
- Onboarding flow 48h détaillé (`onboarding/flow-48h.md`)
- Voice catalog framework (`voices/CATALOG.md`)
- Cross-link J4P documenté (`CROSS-LINK-J4P.md`)

🔶 **Attente Pat / décision** :
- Approbation pricing tiers
- Sélection 4 voices ElevenLabs pour Annie (médical/dentaire/légal/immobilier)
- Signup Vapi (gratuit start)
- Signup Twilio (pay as you go)
- Décision : pilot partners à -25% ou tarifs pleins direct ?

🔴 **Prérequis avant premier client** :
- API keys dans `.env` : `VAPI_API_KEY`, `TWILIO_*`, `DEEPGRAM_API_KEY` (en plus de ELEVENLABS + ANTHROPIC déjà setup)
- Numéro Twilio acheté (région du premier client)
- 1 voice sélectionnée + verrouillée minimum

## Structure du dossier

```
tl-voice-services/
├── README.md                          ← ce fichier
├── CROSS-LINK-J4P.md                  ← intégration avec TL J4P
├── vapi-config/
│   └── receptionist-base.json         ← template config Vapi
├── scripts/
│   ├── 01-medical.md                  ← script Annie clinique médicale
│   ├── 02-dentaire.md                 ← script Annie clinique dentaire
│   ├── 03-legal.md                    ← script Annie cabinet d'avocats
│   └── 04-immobilier.md               ← script Annie courtier immobilier
├── pricing/
│   └── structure-2026-06.md           ← 3 tiers receptionist + voice over + cloning
├── onboarding/
│   └── flow-48h.md                    ← onboarding 0 → live en 48h
├── voices/
│   └── CATALOG.md                     ← framework sélection voices ElevenLabs
├── skills/                            ← (futurs Hermès skills, vide)
└── memory.md, project.json            ← état opérationnel
```

## Sous-agents Hermès (à activer)

| Sous-agent | Rôle | Modèle / Tech | Status |
|------------|------|---------------|--------|
| `voice-synth` | Synthèse voice ElevenLabs (avec FORBIDDEN_VOICES guard) | ElevenLabs API | scaffold |
| `voice-clone-mgr` | Gère voice clones clients (consentement + storage) | ElevenLabs Voice Lab | à créer |
| `receptionist-router` | Route appels entrants → script approprié | Vapi + Twilio | scaffold |
| `voice-agent-conv` | Voice agent conversationnel commerce | Vapi + Claude/GPT | futur |
| `onboarding-bot` | Onboarding automation (V2, post-3 clients) | Custom Python | futur |

## Stack technique

| Couche | Tech | Coût | Status |
|--------|------|------|--------|
| TTS principal | ElevenLabs Pro | $22/mo (actif) | ✅ |
| Voice cloning | ElevenLabs Voice Lab | inclus Pro | ✅ |
| Backup TTS | MiniMax Speech-02 | $13/mo (planned) | 🔶 |
| Telephony orchestration | Vapi | pay as you go, free tier OK démarrage | 🔴 signup needed |
| Telephony provider | Twilio | pay as you go, ~$25/mo prod | 🔴 signup needed |
| Speech-to-text | Deepgram nova-2 | ~$5-10/mo | 🔴 signup needed |
| LLM brain | Claude Sonnet 4.6 via Anthropic direct | ~$10/mo per client | ✅ ($200 backup) |
| Recording / QA | Vapi built-in | inclus | ✅ |

## Économie unitaire (Receptionist Professional $449/mo)

- **Revenus** : $449/mo par client
- **Coûts variables (600 appels/mo)** : ~$85/mo
  - ElevenLabs : ~$15
  - Vapi : ~$30
  - Twilio : ~$25
  - Anthropic Claude : ~$10
  - Infra amortie : ~$5
- **Marge brute** : ~$364/mo (81%)

**Cible MRR** :
- Juillet 2026 : 3-5 clients = $1 350 - $2 245 MRR
- Août 2026 : 8-12 clients = $3 590 - $5 390 MRR
- Décembre 2026 : 25-50 clients = $11 225 - $22 450 MRR

## Blockers actuels (en ordre de priorité)

1. **Pat signup Vapi + Twilio + Deepgram** (~30 min total, plans gratuits OK pour démarrer)
2. **Pat approuve pricing** (lire `pricing/structure-2026-06.md`, ajuster si besoin)
3. **Pat sélectionne 4 voices ElevenLabs** (~30 min écoute catalogue)
4. **Pat enregistre 30 sec voix → ElevenLabs clone pat_custom** (déjà dans todos, pour C3 + voice over Pat)
5. **Identifier 3 pilot partners** (Mauricie, 1 par secteur idéalement) — pour les 3 premiers à -25%

## Prochaine milestone

- **Semaine 9-15 juin** : Vapi + Twilio configurés, 1 voice sélectionnée, 1 pilot partner signé
- **Fin juin** : premier client payant tarif plein
- **Fin juillet** : 3-5 clients actifs

## Notes importantes

- **Le marché QC est mature pour receptionist IA** (selon Pat). Pas besoin d'éduquer le marché — vendre directement le produit.
- **La voix Pat est trop personnelle pour receptionist générique** — `pat_custom` voice est réservée à TL Faceless YT + voice over premium.
- **L'invisibilité de TL Voice** est intentionnelle — client voit J4P, pas TL Voice. Voir `CROSS-LINK-J4P.md`.
- **Compliance Loi 25 Québec** est intégrée dans tous les scripts (auto-identification IA, consentement enregistrement annoncé).
- **TL Voice peut alimenter Phase 2 (mission enseigner)** via voice clones de Pat pour les cours IA + KDP audiobook versions.

## Liens externes

- [ORG_CHART du repo principal](../../ORG_CHART.md)
- [Vapi docs](https://docs.vapi.ai/)
- [ElevenLabs API](https://elevenlabs.io/docs/api-reference/text-to-speech)
- [Twilio Voice docs](https://www.twilio.com/docs/voice)
- [Deepgram API](https://developers.deepgram.com/)
