# Onboarding Flow — Premier client AI Receptionist (48h)

> Cible : 0 → live en 48h depuis signature du contrat
> Garantie temps : si on dépasse 72h, mois 1 gratuit
> Responsable : Pat (jusqu'à automation TL Voice)

---

## H0 — Signature contrat + paiement

**Trigger** : client paye via Stripe (link envoyé par Pat ou via J4P landing).

**Actions automatiques (Stripe webhook)** :
1. Reçu envoyé client
2. Lead créé en CRM avec status « ONBOARDING »
3. Notification Pat (SMS + email)
4. Email automatique « Bienvenue chez [BRAND] — étapes prochaines » envoyé au client
5. Lien Calendly envoyé : booking call onboarding (slot dans les 4h)

---

## H+1h à H+4h — Call de découverte (15 min)

**Format** : Zoom ou téléphone, 15 min max.

**Agenda** :
1. (2 min) Présentation Pat — qui je suis, ce qu'on fait
2. (5 min) Profil client : type d'entreprise exact, structure, heures, volume appels actuel
3. (5 min) Pain points spécifiques : que se passe-t-il aujourd'hui avec leurs appels ? Quoi rater ? Quoi améliorer ?
4. (3 min) Confirmation tier + add-ons + timeline

**Livrables Pat** :
- Notes structurées remplies dans CRM
- Choix du script secteur confirmé (médical/dentaire/légal/immobilier)
- Liste customisations spécifiques notée

---

## H+4h à H+12h — Configuration technique

**Pat (ou agent TL Voice automation à terme) configure** :

1. **Création projet Vapi** :
   - Cloner template `vapi-config/receptionist-base.json`
   - Adapter avec : `NOM_ENTREPRISE`, `NOM_AGENT`, script secteur, intégrations
   - Tester appel sortant interne

2. **Provisionnement numéro Twilio** :
   - Acheter numéro local dans région du client (indicatif Mauricie = 819, etc.)
   - Configurer routing : appel entrant → Vapi → Annie
   - Configurer voicemail fallback

3. **Choix voix ElevenLabs** :
   - Présenter 2-3 options voix matching secteur
   - Client choisit → voix verrouillée dans config

4. **Customisation script** :
   - Adapter messages avec données client (heures, prix de base, etc.)
   - Si customisation = >2h, négocier add-on
   - Validation client par email/audio sample

5. **Intégrations** :
   - Connexion calendrier (Google Cal, Outlook, ou CRM client)
   - Notifications SMS au numéro client
   - Webhooks vers CRM si Business tier

---

## H+12h à H+24h — Tests internes

**Pat fait 5 appels de test minimum** :

1. RDV régulier (scénario typique 1)
2. Urgence claire (test du triage)
3. Confusion volontaire (test recovery)
4. Demande hors-scope (test redirection gracieuse)
5. Appel à 3h du matin (test 24/7 si Professional+)

**Critères pass** :
- ✅ Voix sonne pro et naturelle
- ✅ Pas de boucle infinie dans le dialogue
- ✅ Information critique correctement saisie
- ✅ Routing fonctionne (calendrier ou message reçu)
- ✅ Auto-identification IA présente
- ✅ Conformité Loi 25 + enregistrement annoncé

**Si fail** : retour à H+4h pour ajustements.

---

## H+24h à H+36h — Validation client

**Email envoyé au client avec** :
- Lien vers 3 enregistrements de tests (cas typiques)
- Numéro de test pour appeler eux-mêmes (Annie est live mais routée vers test pendant 12h)
- Formulaire feedback rapide : OK / À ajuster / Quoi changer

**Si ajustements demandés** : pas plus de 2h de tweaks. Sinon, prochaine itération en V2.

**Validation finale** : email confirmation client + signature digitale OK.

---

## H+36h à H+48h — Go live

**Pat exécute** :
1. Port du numéro principal client (si demandé) OU forward du numéro existant client → numéro Twilio
2. Activation mode production Vapi
3. Notification client : « Annie est live, voici comment vérifier que ça marche »
4. Premier rapport quotidien programmé pour J+1 (résumé appels reçus)

**Premier feedback à 48h post-live** :
- Email automatique avec stats première journée
- Demande feedback structuré

---

## J+7 — Check-in suivi

**Pat appelle/email** :
- Tout va bien ?
- Stats première semaine : appels reçus, résolution, satisfaction
- Upsell potentiel : Professional → Business, ajouter voice clone, etc.
- Demande référence si satisfait (1 mois gratuit incitatif)

---

## J+30 — Renouvellement / Upsell

**Trigger** : renouvellement Stripe automatique + email check-in :
- Stats du mois (appels, résolution, conversion si tracking sales)
- Témoignage si satisfait
- Demande référence (1 mois gratuit pour eux + pour le référé)

---

## Échecs / Edge cases

### Client annule pendant onboarding (avant go live)

- Remboursement 100% setup fee si annulation <48h
- Remboursement 50% setup fee si annulation entre 48h-7 jours
- Aucune mensualité si annulation avant go live

### Bug critique post-go live

- Pat (ou astreinte TL Voice) répond dans l'heure
- Si bug ne peut pas être résolu en 4h : fallback humain (numéro forward vers vraie réceptionniste/voicemail) jusqu'à résolution
- Crédit du mois si downtime >24h

### Client non-satisfait après 30 jours

- Refund 30 jours garanti (mois 1 seulement)
- Postmortem honnête : qu'est-ce qui n'a pas marché ?
- Apprentissage intégré dans process et scripts

---

## Métriques Onboarding

- **Time-to-live** : cible <48h, hard ceiling 72h
- **% clients live à J+2** : cible 95%
- **% clients toujours actifs à J+30** : cible >85%
- **NPS post-30j** : cible >50
- **% upsells dans les 90 premiers jours** : cible 30%

---

## Prochaines automations (V2)

À mesure que volume client augmente, automatiser :
- Provisioning Twilio (API)
- Setup Vapi (API) avec scripts pré-validés
- Tests automatisés (suite Vapi simulator)
- Onboarding sans Pat intervention humaine (juste validation finale)

**Cible V2** : Pat n'intervient que pour les Business tier ou cas spéciaux. Starter + Professional auto-onboarding.
