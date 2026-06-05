# Voice Catalog — TL Voice Services

> Sélection de voix ElevenLabs recommandées par secteur + use case
> **Règle absolue** : JAMAIS de default ElevenLabs voice. Toujours une voix sélectionnée/clonée.

## Voices recommandées (à valider/cloner)

### Catégorie A — Annie Réceptionniste (féminine, FR-CA, professionnelle)

| Voice candidate | Use case primaire | Note |
|-----------------|-------------------|------|
| **TBD-1 (à sélectionner)** | Médical + Dentaire | Mature warm professional. Niveau confiance haut. |
| **TBD-2 (à sélectionner)** | Légal + Notaire | Plus formelle, posée. Discrétion en signature. |
| **TBD-3 (à sélectionner)** | Immobilier | Plus dynamique, sourire dans la voix. Chaleureuse. |
| **TBD-4 (à sélectionner)** | Général backup | Versatile, peut servir pour tout secteur. |

**Processus de sélection (à faire avec Pat)** :
1. Pat écoute 10-15 voices ElevenLabs catalogue FR-CA
2. Sélectionne 4 voices pour les 4 use cases ci-haut
3. Test live de chaque voix avec premier script secteur
4. Verrouille les voice_id dans `vapi-config/voice-mapping.json` (à créer)

### Catégorie B — Voice over commercial (catalogue varié)

| Voice | Style | Use case |
|-------|-------|----------|
| **TBD-VO-1** | Annonceur publicitaire FR-CA | Pubs radio/TV |
| **TBD-VO-2** | Narrateur corporatif FR | Vidéos entreprise, e-learning |
| **TBD-VO-3** | Annonceur EN-US | Pubs US, audiobook EN |
| **TBD-VO-4** | Narrateur cinématique EN-UK | Documentaire, audiobook |
| **TBD-VO-5** | Voix conversationnelle FR-CA | Podcast, contenus naturels |

### Catégorie C — Voice clones clients (sur demande)

Géré dans ElevenLabs Voice Lab. Workflow :
1. Client envoie 30+ min audio source (selon tier)
2. Pat (ou tech TL Voice) uploade dans ElevenLabs Voice Lab
3. Voice clone créé + tuning
4. Test avec client → validation
5. Voice_id remis au client OU intégré dans son produit J4P (si réceptionniste avec voix custom)

**Important** :
- Consentement écrit OBLIGATOIRE avant clone (template juridique à créer)
- Voice clone client RESTE propriété du client
- Pat / TL Voice peut PAS utiliser pour autres usages sans consentement explicite

### Catégorie D — Pat voice clone (`pat_custom`)

Voice clone de Pat pour TL Faceless YT + cas spéciaux où la signature Pat est désirée.

**Statut** : à enregistrer (30 sec voix → ElevenLabs clone).
**Use cases** :
- C3 Stacklab tutorials (canal YT)
- Newsletter audio version si lancée
- Voice over personnel
- **NE PAS** utiliser comme voice de réceptionniste générique (la voix Pat est trop personnelle)

## Règles de sélection

1. **Toujours tester en condition réelle** avant de fixer une voix
2. **Vérifier le speaking rate** : 0.9-1.2 pour Annie, 0.95-1.05 pour voice over
3. **Évaluer la fatigue auditive** : faire jouer 5 min de la voix d'affilée, est-ce que ça tient ?
4. **Diversité voice across produits** : éviter que tous les clients aient la même voix (sauf si demande explicite)
5. **Conformité accent / langue** : Vrai français-québécois pour QC, vrai français-européen pour FR EU, jamais l'inverse

## Mapping voice_id (à compléter une fois sélection faite)

```json
{
  "annie_medical": "",
  "annie_dentaire": "",
  "annie_legal": "",
  "annie_immobilier": "",
  "annie_general": "",
  "vo_pub_fr_ca": "",
  "vo_corp_fr": "",
  "vo_pub_en_us": "",
  "vo_doc_en_uk": "",
  "vo_conv_fr_ca": "",
  "pat_custom": ""
}
```

## Liens

- [README](../README.md)
- [Vapi base config](../vapi-config/receptionist-base.json)
- [Scripts secteurs](../scripts/)
