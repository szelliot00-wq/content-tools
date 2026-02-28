# content-tools

Personal automation project. Three tools that monitor content sources and email digests to Steve, all running on a dedicated MacBook Pro.

---

## What this project does

| Tool | What it does |
|---|---|
| youtube-summarizer | Fetches transcripts from YouTube channels, summarises with Gemini, emails digest |
| article-reader | Fetches RSS feeds + manual URLs, summarises with Gemini, emails digest |
| competitor-tracker | Scrapes competitor pages, diffs against saved snapshots, summarises changes, emails digest |

All three run daily at 08:00 via a single launchd job on a dedicated MacBook Pro. An email is only sent if there is something new to report.

---

## Infrastructure

- **Runner machine:** MacBook Pro (headless, external monitor not required day-to-day)
- **Scheduler:** macOS launchd — single agent `com.steveelliott.content-tools`
- **Entry point:** `run-all.sh` — calls all three tools in sequence; a failure in one does not stop the others
- **Current Mac (Steve's main machine):** no scheduled jobs — used only for editing config and code
- **Note:** launchd fires only when the Mac is awake. If the machine is asleep at 08:00 the job is skipped. Keep it plugged in; unplugging briefly to move it is fine as long as it's back and awake before 08:00.

---

## Project structure

```
content-tools/
├── CLAUDE.md
├── requirements.txt
├── run-all.sh                    ← single entry point, called by launchd
├── cron.log                      ← combined log for all three tools (not committed)
├── .env                          ← secrets (not committed)
├── .env.example                  ← template
│
├── shared/
│   ├── summarizer.py             ← Gemini API wrapper (gemini-2.5-flash)
│   ├── email.py                  ← SMTP email sender (Gmail)
│   └── heartbeat.py              ← failure alert email (called by run-all.sh on error)
│
├── youtube-summarizer/
│   ├── summarize.py              ← main script (yt-dlp + youtube-transcript-api + Gemini)
│   ├── creators.json             ← YouTube channels to monitor
│   ├── send_digest.py            ← emails digest of newly committed summaries
│   ├── run.sh                    ← shell wrapper (git pull → run → commit → push → email)
│   ├── summaries/                ← one .md per video summary (committed)
│   └── transcripts/              ← one .txt per transcript (committed)
│
├── article-reader/
│   ├── fetch.py                  ← main script
│   ├── sources.json              ← RSS feeds and manual URLs to monitor
│   └── run.sh                    ← shell wrapper (git pull → run → commit → push)
│
├── competitor-tracker/
│   ├── scrape.py                 ← main script
│   ├── competitors.json          ← competitors and URLs to monitor
│   ├── snapshots/                ← one .txt snapshot per competitor URL (committed)
│   └── run.sh                    ← shell wrapper (git pull → run → commit → push)
│
└── summaries/
    ├── articles/                 ← one .md per summarised article (committed)
    └── competitors/              ← one .md per competitor change event (committed)
```

---

## Configuration files

### article-reader/sources.json

Defines RSS feeds and manual URLs. Structure:

```json
{
  "rss_feeds": [
    {
      "name": "Display name",
      "url": "https://example.com/feed.xml",
      "enabled": true,
      "max_items": 3,
      "cutoff_days": 7
    }
  ],
  "manual_urls": [
    {
      "url": "https://example.com/page",
      "title": "Display title"
    }
  ]
}
```

- `cutoff_days: null` disables date filtering (fetches regardless of age)
- Articles already summarised are skipped by slug match against `summaries/articles/`

### competitor-tracker/competitors.json

Defines competitors and which pages to monitor. Structure:

```json
{
  "competitors": [
    {
      "id": "competitor-id",
      "name": "Competitor Name",
      "enabled": true,
      "urls": [
        { "url": "https://example.com/pricing", "label": "Pricing page" },
        { "url": "https://example.com/features", "label": "Features page" }
      ]
    }
  ]
}
```

- Snapshots are stored as `snapshots/{id}-{label-slug}.txt`
- First run creates baseline snapshot — no email sent
- Changes below 50 chars (`DIFF_THRESHOLD`) are ignored as noise

---

## Environment variables

All secrets live in `.env` (loaded via python-dotenv). See `.env.example`:

```
GEMINI_API_KEY=
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=you@gmail.com
SMTP_PASSWORD=           ← Gmail app password (not account password)
FROM_EMAIL=
EMAIL_TO=
```

**Important:** `SMTP_PASSWORD` must be a Gmail App Password. Go to Google Account → Security → 2-Step Verification → App Passwords.

---

## Scheduling (launchd)

One launchd agent on the MacBook Pro at `~/Library/LaunchAgents/com.steveelliott.content-tools.plist`.

Calls `run-all.sh` at 08:00 daily. Log goes to `cron.log` at the project root.

**launchd commands (run on MacBook Pro):**

```bash
# Reload after editing the plist
launchctl unload ~/Library/LaunchAgents/com.steveelliott.content-tools.plist
launchctl load ~/Library/LaunchAgents/com.steveelliott.content-tools.plist

# Run immediately (test without waiting for schedule)
launchctl start com.steveelliott.content-tools

# Check it's registered
launchctl list | grep steveelliott

# Watch log live
tail -f ~/Claude-projects/content-tools/cron.log
```

---

## Shared modules

### shared/summarizer.py

```python
from shared import summarizer as gemini
summary = gemini.summarize(text, prompt_template)
```

- Uses `gemini-2.5-flash` via `google-genai`
- `{content}` in the prompt template is replaced with the text
- Truncates input at 120,000 chars
- Returns `None` if `GEMINI_API_KEY` is not set

### shared/email.py

```python
from shared import email as mailer
mailer.send_digest(subject="...", items=[{"title": ..., "content": ..., "url": ...}])
```

- Sends HTML + plain text multipart email via Gmail SMTP (port 587, STARTTLS)
- `content` field is rendered as Markdown in the HTML version
- Reads `EMAIL_TO`, `SMTP_USER`, `SMTP_PASSWORD`, `FROM_EMAIL` from environment

---

## How to run manually

On the MacBook Pro:

```bash
cd ~/Claude-projects/content-tools
source .venv/bin/activate

# Run all three tools (same as launchd does)
bash run-all.sh

# Or run individually
python youtube-summarizer/summarize.py
python article-reader/fetch.py
python competitor-tracker/scrape.py

# Single video (for testing)
python youtube-summarizer/summarize.py --video-url https://www.youtube.com/watch?v=VIDEO_ID
```

---

## Dependencies

```
python-dotenv
feedparser
trafilatura
requests
beautifulsoup4
google-genai
youtube-transcript-api>=0.6.0
yt-dlp>=2024.1.0
```

Install: `pip install -r requirements.txt`

Virtual environment: `.venv/` at project root, activated in all run scripts.

---

## Output conventions

- Article summaries: `summaries/articles/YYYY-MM-DD-{url-slug}.md`
- Competitor summaries: `summaries/competitors/YYYY-MM-DD-{competitor-id}.md`
- Competitor snapshots: `competitor-tracker/snapshots/{id}-{label-slug}.txt`
- All output files are committed to git by the individual run scripts

---

## Deploying changes to the MacBook Pro

`run-all.sh` pulls the latest repo and runs `pip install -r requirements.txt` at the top of every run. This means:

- New tool scripts, Python modules, config files, and dependencies are picked up **automatically** on the next scheduled run — no manual steps needed.
- Changes to `run-all.sh` itself take effect on the **run after next** (bash cannot reload a script mid-execution, so the pull happens but the new version of the file runs the following day).

**The only time you need to touch the MacBook Pro** is the very first time after a fresh clone or if the venv is missing. In that case:

```bash
cd ~/Claude-projects/content-tools
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

---

## What not to break

- The slug-based deduplication in `article-reader/fetch.py` prevents re-summarising the same article. Do not change the slugify logic without also migrating existing summary filenames.
- Competitor snapshots must stay in sync with live pages. If you delete a snapshot, the next run treats that URL as a first run and creates a new baseline without sending an email.
- Tool run scripts source `.env` implicitly via python-dotenv inside the Python scripts. If adding new shell-level env var checks, explicitly source `.env` in the shell script first.
- `run-all.sh` uses `$HOME` for paths — do not hardcode `/Users/steveelliott`.
