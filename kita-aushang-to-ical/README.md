# kita-aushang-to-ical

Convert kindergarten / daycare notices (Schließtage, Feste, Elternabende) into individual iCal files or directly into Google / Outlook Calendar.

## What it does

- Reads photos or text of Kita/Krippe Aushänge.
- Extracts closing days and other events.
- Always includes the facility name in the event title.
- Looks up the official address online once the name is clear.
- Outputs individual `.ics` files (iPhone-friendly) or creates the events directly in a connected calendar.
- Asks instead of guessing (facility name, unclear times, past dates).

## Installation

Ask the agent to install the skill (e.g. “Install the kita-aushang-to-ical skill” or point it at the folder / GitHub URL).

## Usage

Send a photo or text of a Kita notice and ask to turn it into calendar entries, iCal, or `.ics`.

Typical triggers:
- “Wandel das nach iCal”
- “Mach mir Kalendereinträge”
- “Trag die Termine in den Google Kalender ein”

The skill will:
1. Confirm it is a Kita notice.
2. Ask for the facility name if not clear.
3. Extract and classify events (all-day closings vs timed events).
4. Check for past dates and ask if needed.
5. Look up the address.
6. Offer `.ics` files (and ZIP) or direct calendar entry if a connector is available.

## Structure

```
kita-aushang-to-ical/
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
- Delta mode: if used again in the same chat, only new or changed events are generated.

## License

MIT (see repository root if present).
