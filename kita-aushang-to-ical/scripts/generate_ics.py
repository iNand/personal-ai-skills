#!/usr/bin/env python3
"""Generate individual RFC5545 .ics files from structured Kita closing events.

Usage:
  python3 generate_ics.py events.json [--out-dir DIR] [--zip NAME]

events.json: list of objects with keys:
  - filename: str (e.g. "2026-12-24_Campus-Kinder-geschlossen.ics")
  - uid: str
  - summary: str
  - description: str
  - location: str
  - allday: bool
  - start: str  # YYYYMMDD or YYYYMMDDTHHMMSS
  - end: str    # YYYYMMDD (exclusive for all-day) or YYYYMMDDTHHMMSS
"""
import argparse
import json
import sys
import zipfile
from pathlib import Path


VTIMEZONE = """BEGIN:VTIMEZONE
TZID:Europe/Berlin
X-LIC-LOCATION:Europe/Berlin
BEGIN:DAYLIGHT
TZOFFSETFROM:+0100
TZOFFSETTO:+0200
TZNAME:CEST
DTSTART:19700329T020000
RRULE:FREQ=YEARLY;BYMONTH=3;BYDAY=-1SU
END:DAYLIGHT
BEGIN:STANDARD
TZOFFSETFROM:+0200
TZOFFSETTO:+0100
TZNAME:CET
DTSTART:19701025T030000
RRULE:FREQ=YEARLY;BYMONTH=10;BYDAY=-1SU
END:STANDARD
END:VTIMEZONE"""


def fold(line: str) -> str:
    """RFC 5545 line folding at 75 octets."""
    if len(line.encode("utf-8")) <= 75:
        return line
    parts = []
    raw = line
    while raw:
        buf = ""
        for ch in raw:
            trial = buf + ch
            if len(trial.encode("utf-8")) > 75:
                break
            buf = trial
        parts.append(buf)
        raw = raw[len(buf):]
        if raw:
            raw = " " + raw
    return "\r\n".join(parts)


def make_ics(ev: dict, dtstamp: str, prodid: str) -> str:
    lines = [
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        f"PRODID:{prodid}",
        "CALSCALE:GREGORIAN",
        "METHOD:PUBLISH",
        "X-WR-CALNAME:" + ev.get("summary", "Kita geschlossen"),
        "X-WR-TIMEZONE:Europe/Berlin",
    ]
    lines.extend(VTIMEZONE.splitlines())
    lines.append("BEGIN:VEVENT")
    lines.append(f"UID:{ev['uid']}")
    lines.append(f"DTSTAMP:{dtstamp}")
    if ev.get("allday", True):
        lines.append(f"DTSTART;VALUE=DATE:{ev['start']}")
        lines.append(f"DTEND;VALUE=DATE:{ev['end']}")
    else:
        lines.append(f"DTSTART;TZID=Europe/Berlin:{ev['start']}")
        lines.append(f"DTEND;TZID=Europe/Berlin:{ev['end']}")
    lines.append(f"SUMMARY:{ev['summary']}")
    if ev.get("location"):
        lines.append(f"LOCATION:{ev['location']}")
    desc = ev.get("description", "")
    if desc:
        lines.append(f"DESCRIPTION:{desc}")
        lines.append(f"COMMENT:{desc}")
    lines.append("STATUS:CONFIRMED")
    lines.append("TRANSP:OPAQUE")
    lines.append("END:VEVENT")
    lines.append("END:VCALENDAR")
    folded = [fold(l) for l in lines]
    return "\r\n".join(folded) + "\r\n"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("events_json", help="Path to JSON list of events")
    parser.add_argument("--out-dir", default=".", help="Output directory")
    parser.add_argument("--zip", default="kita-icals.zip", help="Zip filename")
    parser.add_argument("--dtstamp", default="20260101T000000Z")
    parser.add_argument("--prodid", default="-//Kita Aushang to iCal//DE")
    args = parser.parse_args()

    events = json.loads(Path(args.events_json).read_text(encoding="utf-8"))
    if not isinstance(events, list) or not events:
        print("No events in JSON", file=sys.stderr)
        sys.exit(1)

    out = Path(args.out_dir)
    out.mkdir(parents=True, exist_ok=True)
    written = []
    for ev in events:
        content = make_ics(ev, args.dtstamp, args.prodid)
        p = out / ev["filename"]
        p.write_bytes(content.encode("utf-8"))
        written.append(p)

    zip_path = out / args.zip
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for p in written:
            zf.write(p, p.name)
    print(f"Wrote {len(written)} .ics + {zip_path}")


if __name__ == "__main__":
    main()
