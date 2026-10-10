# iCal Output Rules

Use together with `scripts/generate_ics.py`.

## Event structure (JSON for the script)

```json
{
  "filename": "2026-12-24_Campus-Kinder-geschlossen.ics",
  "uid": "2026-12-24-weihnachten@facility",
  "summary": "Campus Kinder geschlossen",
  "description": "Weihnachten / Jahreswechsel 24.12.2026–08.01.2027.",
  "location": "Campus Kinder, Amalienstraße 83, 80799 München",
  "allday": true,
  "start": "20261224",
  "end": "20270109"
}
```

- `allday: true` → start/end as YYYYMMDD, end is exclusive (next day after last day).
- `allday: false` → start/end as YYYYMMDDTHHMMSS, TZID Europe/Berlin.
- UID must be unique per event.
- Filename must be safe (no spaces preferred, or use hyphens).

## Calling the script

```bash
python3 scripts/generate_ics.py events.json --out-dir /workspace/artifacts/kita-icals --zip kita-icals.zip
```

Then render the ZIP (and optionally individual files) to the user.

## Common pitfalls

- DTEND for all-day is exclusive → 24.12.–08.01. inclusive needs DTEND of 09.01.
- Handwritten corrections (e.g. extra days) must be flagged and confirmed if unclear.
- Do not invent end times for partial closures beyond the conventional 12:30–18:00 unless the notice states them.
- Always include VTIMEZONE for timed events so iPhone/Android handle Europe/Berlin correctly.
