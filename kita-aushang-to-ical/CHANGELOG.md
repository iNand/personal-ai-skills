## 2026-10-10 (Update 2)
- Mandatory online search for the facility address once the name is known
- Address is stored as LOCATION in every event (and in direct calendar entries)
- If address search is ambiguous or fails: ask user or omit and mention

## 2026-10-10 (Update 1)
- Facility name always included in SUMMARY ("{Name} geschlossen" or "{Name}: {Event}")
- Other events (Feste, Elternabende etc.) included by default
- Reasons for closures always in COMMENT
- Optional direct creation in Google Calendar / Outlook Calendar (after connector auth)

## 2026-10-10
- Initial creation
- Workflow with pre-check for actual Kita closing notices
- Mandatory user confirmation for facility name and past dates (no guessing)
- Individual .ics + ZIP via generate_ics.py
- Based on real Campuskinder notice conversions
