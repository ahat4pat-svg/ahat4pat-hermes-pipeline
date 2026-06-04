# C3 — Vidéo 01 — Build a Lead Scoring Bot with n8n + Claude (20 Minutes)

**Status** : brief prêt, génération pending API keys
**Durée cible** : 12-15 min (sweet spot mid-roll ads + watch time complet)
**Format** : 16:9 horizontal, 1080p min (4K si OBS le permet)
**Voix** : ElevenLabs voix signature C3 (à confirmer Pat : option Hybrid recommandée)

---

## YouTube — Title (SEO)

> *Build a Lead Scoring Bot with n8n + Claude in 20 Minutes (Step by Step)*

Variations A/B :
- *I Built a Lead Scoring Bot in 20 Minutes (n8n + Claude Workflow)*
- *n8n + Claude — Score Every Lead Automatically (Free Template)*
- *Your Inbox Should Be Scoring Leads For You (Here's How)*

## YouTube — Description

```
In 20 minutes, you'll build an n8n automation that reads every incoming email, scores the sender as Hot / Warm / Cold using Claude, and routes the hot ones to Slack while logging everything to Notion.

No code. No SaaS lead scoring tool. Just n8n + Claude + 4 nodes.

The complete workflow JSON is in the description — copy, paste, configure.

⏱️ TIMESTAMPS
00:00 — Why your inbox should be doing this
00:45 — n8n setup overview (skip if you have it)
02:30 — Gmail trigger node
04:00 — Claude scoring node (prompt walkthrough)
07:30 — Conditional routing logic
09:30 — Slack alert for HOT leads
11:00 — Notion logging for ALL leads
13:00 — Live test with 5 real emails
15:00 — Edge cases + tuning the prompt

🛠️ TOOLS USED
→ n8n (self-hosted or cloud) : https://n8n.io/?ref=AHAT4PAT
→ Claude API (Anthropic) : https://anthropic.com/?ref=AHAT4PAT
→ Notion : https://notion.so/?ref=AHAT4PAT
→ Slack (free tier works) : —

📦 FREE WORKFLOW JSON DOWNLOAD
→ Link in description : github.com/ahat4pat/n8n-lead-scoring-bot

🎯 THIS VIDEO IS PART OF A SERIES
Building the Solo Operator Stack — 10 automations that buy your time back.
Subscribe to catch every drop.

#n8n #claudeai #automation #leadgeneration #nocode #solopreneur #aitools #productivity
```

## YouTube — Tags

```
n8n tutorial, claude api tutorial, lead scoring automation, n8n claude integration, ai lead scoring, n8n workflow tutorial, no code automation, anthropic claude, inbox automation, gmail automation n8n, solopreneur tools 2026, ai for solopreneurs, automated lead qualification, indie hacker automation, claude opus tutorial, n8n self hosted, ai operator stack
```

---

## ElevenLabs — Full voice script (~2200 mots)

> Coller dans ElevenLabs avec voix signature C3 (à choisir : recommend "Adam" ou "Daniel" — confident neutral male EN, ou "Charlotte" si feminine signature préférée). Generation par chunks de 500 mots si voix grise.

### Section 1 — Hook (0:00-0:45, ~120 mots)

```
You're getting too many emails. Most of them are noise. A few of them are gold. The problem? You can't tell them apart until you read them. And reading takes time. Hours. Every. Day.

What if your inbox could do that for you? Score every sender. Tell you who's actually worth a reply. Quietly. In the background. Without you opening a single message.

In the next 20 minutes, I'll show you exactly how to build that — with n8n, Claude, and four simple nodes. No code. No expensive SaaS. The full workflow is in the description for you to copy. Let's build.
```

### Section 2 — n8n Setup overview (0:45-2:30, ~280 mots)

```
First, let's get aligned on n8n. If you already have it running, skip to two minutes thirty in the timestamps below.

For everyone else — n8n is an automation tool. Think of it as Zapier you actually own. You can run it in the cloud for fifteen bucks a month, or self-host on a five dollar VPS like Hetzner. I'm running self-hosted, but everything in this video works identically on cloud.

The key concept : workflows are made of nodes. Each node does one thing — listen for an event, transform data, send it somewhere. You connect them with arrows. Data flows left to right.

For this lead scorer, we need four nodes :

One — a Gmail trigger that fires whenever a new email arrives.
Two — a Claude node that reads the email and assigns a score.
Three — a conditional that says : if Hot, alert Slack ; otherwise, just log.
Four — a Notion node that records every lead with its score in a database.

That's it. Four nodes. Twenty minutes. You'll have a working bot at the end of this video.

Open n8n. Hit "new workflow" in the top right. Name it "Lead Scorer V1". And let's start building.
```

### Section 3 — Gmail trigger node (2:30-4:00, ~250 mots)

```
First node — Gmail trigger.

Click the plus button in the workflow canvas, type "gmail", and select "Gmail Trigger".

Now you need to connect your Gmail account. This is the only credential step that takes effort — Google requires a one-time OAuth setup. Click "create new credential", then follow the popup. If you've never done this, the n8n docs walk through it in five minutes.

Once connected, configure the trigger :

Event : choose "New Email"
Mailbox : INBOX
Trigger time : every five minutes works well for most people. If you're a high-volume operator, every minute is fine.

Now — this part matters — filter on "From Address" doesn't contain "no-reply" or "noreply". You don't want to score Stripe receipts and password resets. Add a filter rule for that.

Hit "Test step". n8n will pull the most recent unfiltered email from your inbox so you can see the data structure. You should see a JSON object with the from address, subject, body, and a few metadata fields.

Right click the from address field and select "Use in next node". This tells n8n to pass that value forward. Same for subject and body.

Now we have an email triggering the workflow. Next, we score it.
```

### Section 4 — Claude scoring node (4:00-7:30, ~520 mots)

```
This is where the magic happens.

Add a new node. Search "anthropic". Select the Anthropic Claude node.

Connect your Claude API key. If you don't have one, sign up at anthropic.com slash console — the link is in my description with a referral. Five dollars in credits gets you about a thousand lead scorings.

Now configure the node :

Operation : "Message a model"
Model : "claude-opus-4-7" — Opus gives the best scoring quality. If you want to optimize cost, swap to "claude-haiku-4-5" later — it's six times cheaper and almost as accurate for this task.

Then the system prompt. This is the core of the bot. Here's the prompt I use — pause the video if you want to copy it from the screen.

```
You are a lead scoring assistant for a solo consultant. Given the email content, output a single JSON object:

{
  "score": "HOT" | "WARM" | "COLD",
  "reason": "<one sentence explaining the score>",
  "follow_up": "<one suggested next action>"
}

Scoring rules:

HOT — sender explicitly asks for a call, demo, proposal, or pricing. Sender mentions a specific budget, deadline, or use case. Sender represents a company or has a verifiable LinkedIn / domain.

WARM — sender asks a question that implies interest but no commitment. Sender introduces themselves or asks "are you taking new clients". Sender is on a free tier of a product you sell.

COLD — sender is offering YOU something (SEO, design, leads). Sender is on a marketing list. Sender is asking a generic question with no buying signal.

Output ONLY the JSON object. No prose.
```

In the user prompt field, drag in the email body and subject from the trigger node. Like this :

```
Subject: {{$json.subject}}

From: {{$json.from}}

Body:
{{$json.body}}
```

The double curly brace syntax is n8n's way of injecting data from previous nodes.

Hit "Test step". You should get back a JSON object with score, reason, and follow_up. Beautiful.

A tip on tuning : if Claude is being too generous with HOT scores, add to your rules : "Default to WARM unless there is explicit buying signal." If it's too cold, add : "Err on the side of WARM when ambiguous." You'll iterate this prompt over the first week as you watch real scores come in.

We have a scored lead. Now we route.
```

### Section 5 — Conditional routing (7:30-9:30, ~280 mots)

```
Add an "IF" node. This is n8n's conditional.

Configuration :

Condition 1 :
  Left value : drag in the score field from the Claude output
  Comparison : "equals"
  Right value : type "HOT"

That's it. One condition. The IF node will now have two output branches : true on top, false on bottom.

True means HOT — we'll alert Slack.
False means WARM or COLD — we'll just log to Notion.

Both branches will end up in Notion eventually, because we want a full audit trail. But only HOT pings Slack in real time.

A note on why this matters strategically : the value of this bot isn't just speed — it's filtering. Most operators get good leads but lose them in inbox noise. By alerting on HOT only, you give yourself a clear signal channel. When Slack pings you with a HOT lead, you reply within minutes. That response speed alone wins deals that slower competitors lose.

The conditional logic is simple, but the discipline of acting fast on HOT is what makes the bot pay for itself in week one.

Drag the true output toward the right of the canvas — we'll attach a Slack node there next.
```

### Section 6 — Slack alert for HOT (9:30-11:00, ~220 mots)

```
Add a Slack node. Operation : "Send a message".

Connect your Slack workspace. You'll need to create a Slack app and get a webhook URL — n8n has a wizard for this, takes three minutes.

Configure :

Channel : #hot-leads (create this channel first in Slack — keep it focused, just you and maybe a partner)

Message body :
```
🔥 HOT LEAD
From: {{$json.from}}
Subject: {{$json.subject}}

Reason: {{$json["Claude"].score.reason}}
Suggested follow-up: {{$json["Claude"].score.follow_up}}

Open in Gmail: https://mail.google.com/mail/u/0/#inbox/{{$json.threadId}}
```

That last line is the kicker — it's a direct deep link to the Gmail thread, so when Slack pings you, one tap opens the full email in your browser. Speed compounds.

Test the node. You should see a fake message appear in #hot-leads if you have a HOT email in your test data. If you don't, force a HOT manually : edit the Claude output in n8n's test panel before running the IF node, set score to HOT, and re-run.

Looks good ? Let's add the Notion logging.
```

### Section 7 — Notion logging (11:00-13:00, ~280 mots)

```
Before this node, set up a Notion database called "Lead Score Log". Columns :

- Date (Date type)
- From (Email or Text)
- Subject (Text)
- Score (Select : HOT, WARM, COLD)
- Reason (Text)
- Follow_up (Text)
- Status (Select : New, Replied, Closed, Ghosted)

Save that Notion database, copy its ID from the URL.

Now back in n8n, add a Notion node. Operation : "Create a database page".

Connect Notion. Paste the database ID.

Map the fields :

Date → {{$now}}
From → {{$json.from}}
Subject → {{$json.subject}}
Score → drag in the score from Claude output
Reason → drag in the reason
Follow_up → drag in follow_up
Status → "New" (default)

Connect this node to BOTH branches of the IF — true and false. Click the connecting arrow on the false branch, then drag it from the conditional to the Notion node. This way, every lead ends up in Notion regardless of score.

Test the node. Open Notion. You should see a new row with the lead data populated.

Beautiful. Now we activate the workflow and watch it run.
```

### Section 8 — Live test (13:00-15:00, ~280 mots)

```
Top right of n8n — toggle "Active" to on.

The workflow is now live. It'll fire every five minutes against your real inbox.

I've prepared five test emails and sent them to my inbox over the last ten minutes. Let me show you the results live.

Open Notion. Refresh.

Five new rows. Let's go through them.

Email one — from "sarah@acme.com" — subject "Looking for a Claude integration consultant for Q3 project" — score : HOT — reason : explicit project + timeline. Slack pinged me thirty seconds ago.

Email two — from "newsletter@designjoy.com" — subject "Five ideas for your business this week" — score : COLD — reason : marketing list. No ping. Just logged.

Email three — from "alex@indie.io" — subject "Quick question about your services" — score : WARM — reason : interest implied, no commitment. No ping. Logged.

Email four — from "growth-tools@daily.com" — subject "Want more SEO traffic ?" — score : COLD — reason : selling to me. Logged.

Email five — from "marc@enterprise.com" — subject "Demo request — team of forty" — score : HOT — reason : specific scale + intent. Slack pinged.

Two HOT leads in five minutes. Both will get a reply from me in under an hour. The other three — I'll check the Notion log at the end of my workday and batch-process WARMs.

That's the bot working.
```

### Section 9 — Edge cases + scaling (15:00 close, ~260 mots)

```
A few notes on tuning over time.

One. The Claude prompt is your bot's brain. Spend twenty minutes a week refining it as you see real scores. Add patterns you notice — like "if sender mentions our podcast, default to WARM minimum because they consumed content already".

Two. The Hot leads channel in Slack should stay narrow. If you start getting more than five HOT pings a day and they're not converting, your prompt is too generous. Tighten it.

Three. Add cost tracking. Claude Opus runs about three cents per lead at current pricing. A hundred leads a day is three dollars a day, which pays for itself if even one extra HOT lead becomes a client per month.

Four. Switch to Haiku as you scale. Once your prompt is tuned and stable, swap "claude-opus-4-7" to "claude-haiku-4-5" in the Claude node. You'll drop cost by six times with negligible accuracy loss for this task.

Five. The next automation in this series builds a follow-up bot that watches the Status column in Notion and sends polite nudge emails for WARMs that go three days without reply. Subscribe to catch it.

The complete workflow JSON is linked in the description. Copy it, configure your credentials, and you have a working lead scorer in your inbox tonight.

If this helped, drop a comment with your use case — I read every one. And tap subscribe for the rest of the Solo Operator Stack series.

I'm Patrick. Talk to you in the next one.
```

---

## OBS Screen recording setup

1. **Resolution** : 1920×1080 minimum (3840×2160 if your Mac supports)
2. **Frame rate** : 30 fps suffit (60 fps si action UI rapide)
3. **Scenes to prepare** :
   - Scene 1 : n8n full window (browser)
   - Scene 2 : n8n + Slack split (for testing section)
   - Scene 3 : Notion database full window
   - Scene 4 : Talking head placeholder (will be replaced by voice-only)
4. **Audio** : capture system audio + voice off track séparé (post-prod overlay)
5. **Mouse highlight** : enable mouse click highlight plugin (yellow circle) for tutorial clarity

## Veo 3.1 — B-roll prompts (3-4 inserts pour breakup screen recording)

### B-roll 1 — Email flood (intro 0:30-0:45)
```
Cinematic shot of a smartphone screen flooded with email notifications, hundreds of preview snippets stacking on top of each other faster than the eye can read, soft blue glow, no people visible, no readable text on screen (pixelated previews), 16:9 horizontal, slow camera push-in, --ar 16:9
```

### B-roll 2 — Workflow diagram animation (3:00 transition)
```
Cinematic animation of a flowchart-style diagram building itself node by node : email icon → AI brain icon → conditional split → Slack icon + Notion icon, clean dark background, neon blue glowing connections, no text, no people, technical aesthetic, slow build, --ar 16:9
```

### B-roll 3 — Hot lead glow (11:30 hot lead alert)
```
Cinematic macro of a smartphone notification banner appearing on a dark home screen with the word HOT in glowing orange, slow rise from the bottom, dark moody background, no other text readable, no people, intimate phone aesthetic, --ar 16:9
```

### B-roll 4 — Dashboard satisfaction (14:30 closing reveal)
```
Cinematic overhead shot of a clean tech workspace at golden hour, a single laptop showing a Notion-style dashboard with green checkmarks scrolling, warm wood desk, one coffee cup, plants in background blurred, no people, no readable on-screen text, satisfying productive vibe, --ar 16:9
```

---

## Suno — Music prompt

```
Style : modern minimal tech ambient, soft electronic pulse, mellow piano accents, gentle warm pad, no vocals, no lyrics, 88-92 BPM, key of E major, 14-15 minute generative track, sits beneath voice without distraction, slow build but no sudden dynamics, productive focus energy, indie hacker vibe.
```

Generate 2-3 variations, pick the one that has consistent energy without dramatic peaks (voice over needs to stay readable).

---

## Midjourney — Thumbnail prompt

```
YouTube thumbnail 16:9 horizontal, clean modern split composition : left half shows a chaotic crowded email inbox with red notification dots overflowing, right half shows a clean Notion-style dashboard with green HOT badge and one orange WARM badge, divider in the middle is a glowing electric blue circuit line, dark mode aesthetic, no people, BIG TEXT overlay "LEAD SCORING BOT" in bold sans-serif at top center, "20 MIN" smaller in bottom right corner, --ar 16:9 --style raw --v 6
```

Backup variation :
```
YouTube thumbnail 16:9, dramatic flat-design composition : a large red "HOT" badge taking center stage, surrounded by smaller gray faded badges saying COLD COLD WARM COLD, on a dark tech-aesthetic background with subtle circuit lines, no people, text overlay "n8n + CLAUDE = AUTO LEAD SCORER" sans-serif bold, --ar 16:9 --style raw --v 6
```

---

## ffmpeg assembly skeleton

```bash
# Assume:
# - OBS screen recording saved as screen.mp4 (1080p, has system audio)
# - Voice over track saved as voice.mp3 (ElevenLabs export)
# - 4 B-roll inserts saved as broll-01.mp4 ... broll-04.mp4
# - Suno music track saved as music.mp3

cd ~/Linux/faceless-yt/C3-ai-tutorials/output/01-n8n-claude-lead-scoring-bot/

# Step 1: extract original screen audio (we'll mute most of it)
ffmpeg -i screen.mp4 -vn -acodec copy screen-audio.m4a

# Step 2: mix music + voice (ducking music when voice present is ideal — use sidechain compression in Audacity for production, but for prototype just lower music volume)
ffmpeg -i music.mp3 -i voice.mp3 -filter_complex \
  "[0]volume=0.18[a];[1]volume=0.85[b];[a][b]amix=inputs=2:duration=longest" \
  -c:a aac mixed-voice-music.aac

# Step 3: replace screen audio with mixed track
ffmpeg -i screen.mp4 -i mixed-voice-music.aac -c:v copy -map 0:v -map 1:a -shortest screen-with-voice.mp4

# Step 4: cut B-roll inserts into timeline at specific timestamps
# (Use DaVinci Resolve OR CapCut for this — too complex for raw ffmpeg)
# Final output: video-01-final.mp4
```

(For first prototype, accepting that the B-roll insertion requires DaVinci or CapCut. Pure ffmpeg can concat shots but precision insertion at timestamps benefits from a real NLE.)

---

## Métriques cibles à 90 jours

- Vues : 5-30K (channel à 0 sub, tech niche has slower start but higher value per view)
- Retention avg : > 55% (tech tutorial benchmark)
- CTR thumbnail : > 6%
- Sub conversion : 2-4% des viewers (tech audience converts higher than entertainment)
- Affiliate clicks : 5-10% of views (Claude API + n8n + Notion stacked)
- First sale conversion : 1-3% des clicks

## Viral hook angles (pour A/B title testing)

- *Build a Lead Scoring Bot with n8n + Claude in 20 Minutes (Step by Step)*
- *I Built a Lead Scoring Bot That Pays for Itself in a Week*
- *Stop Reading Cold Emails — Build This n8n Workflow*
- *Your Inbox Should Be Doing This (n8n + Claude Tutorial)*
- *The Email Bot Every Solo Operator Needs (n8n + Claude, 20 Min)*

---

## Notes pour la production

1. **Voice signature à choisir** : si Pat option Hybrid → générique EN ; si D2 strict → générique aussi ; si D1 bascule → voix Pat clonée ElevenLabs (à enregistrer avec Aokeo + NT1-A après setup voice production)
2. **The "I'm Patrick" sign-off** dans le script est intentionnel — match D1 bascule. Si D2 strict, remplacer par "I'm your indie automation guide" ou similar generic.
3. **Tools mentionnés** TOUS doivent avoir liens affiliate dans description timestamp-mapped
4. **First series video** = la fondation d'une serie "Solo Operator Stack" — chaque vidéo build sur la précédente, force le binge + subscribe
