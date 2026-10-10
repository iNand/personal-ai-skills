# Parsing & Decision Guidelines

Use when extracting from a photo or text of a German Kita/Krippe Schließtage-Aushang.

## Pre-check: Is this a closing schedule?

Look for:
- Title containing Schließtage, Termine, Kita, Krippe, Kindergarten, Campuskinder, etc.
- Lists of dates with labels like Weihnachten, Sommer, Brückentag, Konzeptionstag, Betriebsversammlung, Faschingsdienstag, Teamfortbildung.
- Explicit "Kita geschlossen" or "Krippe schließt nach dem Mittagessen".

If none of these are present (e.g. general flyer, menu, unrelated photo):
- Do **not** auto-apply the skill.
- Only proceed if the user explicitly says "use the skill anyway" / "versuch es trotzdem" / similar.
- Reply with something like: "Dafür bin ich eigentlich nicht optimiert (kein erkennbarer Kita-/Krippen-Schließtage-Aushang), aber ich bemühe mich natürlich trotzdem." Then continue carefully.

If the image/text contains no extractable dates at all:
- Stop and return a clear error: "Im Foto/Text wurden keine Termine oder Schließtage gefunden. Bitte klareres Foto oder die Daten als Text schicken."

## Facility name and address

- Extract the name only if unambiguously written on the notice.
- If missing or ambiguous → `ask_user_question`. Never guess.
- Once the name is clear: **must** search online (`web_search` or `places_search`) for the official address.
- Prefer official sources. If multiple or unclear results → ask the user.
- Use the confirmed address as LOCATION in every event. If none found, omit and mention it.

## Date handling

- Prefer machine-printed dates. Note handwriting separately and flag it.
- Ranges (e.g. 10.–28.08.26) become one multi-day all-day event.
- Partial closures ("schließt nach dem Mittagessen") → timed event starting 12:30 (end 18:00 unless user specifies otherwise).
- Missing dates ("Termin folgt noch") → omit and mention in the summary.
- **Past dates**: Compare to current date. If any extracted date is in the past:
  - Flag it explicitly.
  - Use `ask_user_question` to confirm whether to include it, correct the year, or drop it.
  - Do not silently include or drop.

## Default output rules (recommendations, not hard)

- One .ics per logical event / block (iPhone compatibility).
- Filename starts with YYYY-MM-DD of the start date.
- SUMMARY for closures: "{FacilityName} geschlossen".
- LOCATION: full address if known or provided by user; otherwise omit or ask.
- DESCRIPTION + COMMENT: short reason from the notice (no invention).
- All-day: DTSTART;VALUE=DATE / DTEND;VALUE=DATE (end exclusive).
- Timed: Europe/Berlin with VTIMEZONE.
- Also produce a ZIP of all individual files.

## What to include by default

All recognizable appointments: Schließtage (full and partial) **and** other events (Feste, Elternabende, Weihnachtsfeier etc.).
- Closures: SUMMARY "{Name} geschlossen", reason in COMMENT.
- Other events: SUMMARY "{Name}: {Eventname}".
