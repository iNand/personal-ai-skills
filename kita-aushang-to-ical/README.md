# kita-aushang-to-ical

Convert kindergarten / daycare notices (Schließtage, Feste, Elternabende) into individual iCal files or directly into Google / Outlook Calendar.

Designed for parents who receive photo or paper notices about closing days and events. The skill extracts the dates, always includes the facility name in the event title, looks up the official address, and asks instead of guessing.

## What it does

- Accepts a photo or text of a Kita/Krippe Aushang.
- Extracts closing days (all-day) and other events (timed).
- Puts the facility name into every event title.
- Looks up the official address online once the name is clear.
- Generates individual `.ics` files (easy to import on iPhone) or creates the events directly in a connected Google Calendar or Outlook Calendar.
- Asks the user when the facility name is unclear, times are missing, or dates are in the past.
- Supports delta mode: if used again in the same chat, only new or changed events are generated.

## Installation

**Recommendation:** Before installing any third-party skill (including this one), consider loading [skill-gate](../skill-gate/) first. It performs a static security review of foreign skills before they are activated. See the skill-gate README for the problem it addresses and how to install it.

### Recommended: Ask the agent (copy-paste)

Copy the following message into your chat:

```
Install the kita-aushang-to-ical skill from https://github.com/iNand/personal-ai-skills/tree/main/kita-aushang-to-ical
```

### Alternative 1: Download ZIP

1. Download the repository as ZIP:  
   https://github.com/iNand/personal-ai-skills/archive/refs/heads/main.zip
2. Extract it.
3. Upload or point the agent to the extracted `kita-aushang-to-ical` folder and say:

```
Install the skill from this folder
```

### Alternative 2: Copy the skill text into the chat

1. Open the raw SKILL.md:  
   https://raw.githubusercontent.com/iNand/personal-ai-skills/main/kita-aushang-to-ical/SKILL.md
2. Copy the entire content.
3. Paste it into the chat and say:

```
Create and install a skill from the following SKILL.md content:

[paste content here]
```

## Usage

Send a photo or text of a Kita notice and ask to turn it into calendar entries, iCal, or `.ics`.

Typical prompts:
- “Wandel das nach iCal”
- “Mach mir Kalendereinträge aus dem Aushang”
- “Trag die Termine in den Google Kalender ein”
- “Einzeldateien fürs iPhone”

The skill will:
1. Confirm it is a Kita notice with dates.
2. Ask for the facility name if it is not clearly readable.
3. Extract and classify events (all-day closings vs timed events, including partial closings).
4. Flag past dates and ask for confirmation.
5. Look up the official address.
6. Offer individual `.ics` files (plus a ZIP) or direct calendar entry if a calendar connector is available.

## Structure

```
kita-aushang-to-ical/
├── README.md
├── SKILL.md
├── references/
│   ├── ical-rules.md
│   └── parsing-guidelines.md
├── scripts/
│   └── generate_ics.py
└── evals/
```

## Notes

- Never guesses the facility name or silently includes past dates.
- Prefers official sources for the address.
- If a calendar connector (Google or Outlook) is not connected, the skill will offer a connect card.
- Default output is individual `.ics` files; direct calendar entry only on explicit request.

## License

MIT (see repository root).
