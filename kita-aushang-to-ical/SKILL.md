---
name: kita-aushang-to-ical
description: "Convert kindergarten or daycare notices (Schließtage, Feste, Elternabende) into individual iCal files or directly into Google/Outlook Calendar. Use when the user asks to turn a Kita/Krippe Aushang or photo into calendar entries, iCal, or .ics, or to enter them into a calendar. Always include the facility name in the title. Never guess the name or silently include past dates — ask the user. Not for unrelated photos unless explicitly requested."
type: workflow
lifecycle: active
---

# Kita-Aushang to iCal — Schließtage und Events zuverlässig in Kalender

Wandle Aushänge von Kindertagesstätten / Krippen (Schließtage, Feste, Elternabende) in einzelne .ics-Dateien um oder trage sie auf Wunsch direkt in Google Calendar / Outlook Calendar ein. Name der Einrichtung steht immer im Titel. Keine Raten.

## Wann den Skill verwenden

- Nutzer schickt Foto oder Text eines Kita-/Krippen-Aushangs und will Kalendereinträge, iCal, .ics oder direkt im Kalender.
- Typische Trigger: "Wandel das nach iCal", "mach mir Kalendereinträge", "trag die Termine in den Google Kalender ein", "Einzeldateien fürs iPhone".
- **Nicht** automatisch bei beliebigen Fotos. Nur wenn klarer Aushang oder explizite Nutzeranweisung.

## Workflow (immer in dieser Reihenfolge)

1. **Pre-Check: Ist das ein Kita-/Krippen-Aushang mit Terminen?**
   - Suche nach Schließtage, Kita/Krippe, Feste, Elternabend, Weihnachten, Sommer, Brückentag usw.
   - Wenn nein: Nur auf ausdrückliche Anforderung weitermachen und vorher sagen: "Dafür bin ich eigentlich nicht optimiert, aber ich bemühe mich natürlich trotzdem."
   - Wenn keine Termine erkennbar: Stoppen mit klarer Fehlermeldung: "Im Foto/Text wurden keine Termine gefunden. Bitte klareres Foto oder die Daten als Text."

2. **Einrichtungsname eindeutig machen (Pflicht)**
   - Name muss im Aushang klar und eindeutig lesbar sein.
   - Sonst **sofort** `ask_user_question`. Niemals raten.
   - Der Name steht **immer** im SUMMARY.

3. **Termine extrahieren und klassifizieren**
   - Schließtage (ganztägig) → All-Day-Blöcke, SUMMARY: "{Name} geschlossen", Grund im COMMENT.
   - Teilschließungen ("nach dem Mittagessen") → Timed ab 12:30, SUMMARY: "{Name} geschlossen", Grund im COMMENT.
   - Andere Events (Feste, Elternabende, Weihnachtsfeier etc.) → Timed mit angegebenen Uhrzeiten, SUMMARY: "{Name}: {Eventname}" (z. B. "Campus Kinder: Weihnachtsfeier").
   - Fehlende Daten ("Termin folgt noch") → weglassen und erwähnen.
   - Handschrift und Jahres-Korrekturen flaggen.
   - Details: `references/parsing-guidelines.md`.

4. **Vergangenheits-Check**
   - Jedes Datum gegen aktuelles Datum prüfen.
   - Vergangenheit oder verdächtige Jahreszahl → flaggen und mit `ask_user_question` bestätigen lassen.
   - Niemals stillschweigend übernehmen oder streichen.

5. **Adresse online recherchieren (Pflicht, wenn Name bekannt)**
   - Sobald der Einrichtungsname eindeutig ist: mit `web_search` oder `places_search` die offizielle Adresse suchen (z. B. „Kita {Name} Adresse“, „{Name} Kindertagesstätte Standort“).
   - Bevorzugt offizielle Quellen (Trägerseite, städtische Kita-Liste, Studierendenwerk etc.).
   - Nur die gefundene Adresse als LOCATION eintragen. Wenn mehrere Treffer oder unklar → Nutzer fragen, nicht raten.
   - Wenn nichts gefunden wird: LOCATION weglassen und erwähnen.

6. **Strukturierte Events erzeugen**
   - Pro logischem Termin / Block ein Event.
   - Filename beginnt mit YYYY-MM-DD.
   - SUMMARY immer mit Einrichtungsname.
   - COMMENT/DESCRIPTION: bei Schließungen immer der Grund; bei anderen Events die Kurzbeschreibung.
   - LOCATION = die online recherchierte (oder vom Nutzer bestätigte) Adresse.
   - Regeln: `references/ical-rules.md`.

7. **Ausgabe wählen**
   - Standard: einzelne .ics + ZIP über `scripts/generate_ics.py`.
   - Auf Wunsch ("trag es gleich ein", "Google Kalender", "Outlook"): 
     - Prüfe mit `search_connected_tools`, ob Google Calendar oder Outlook Calendar verbunden ist.
     - Wenn nicht: `request_connector_auth` mit dem gewünschten Connector und kurzem Grund.
     - Wenn verbunden: Termine direkt anlegen (All-Day oder Timed) **inkl. der recherchierten Adresse**.
   - Beide Wege können parallel angeboten werden.

8. **Antwort**
   - Kurze Übersicht der Termine (Schließungen und andere Events getrennt).
   - Explizit: weggelassene Einträge, korrigierte Daten, nachgefragte Punkte, verwendete Adresse.
   - Hinweis auf iPhone-Import der Einzeldateien oder auf den Status der Kalender-Eintragung.

## Was standardmäßig rein kommt

- Alle erkennbaren Termine: Schließtage **und** andere Events (Feste, Elternabende usw.).
- Schließtage bekommen den Zusatz "geschlossen" und den Grund im Kommentar.
- Andere Events bekommen "{Name}: {Event}".

## Kalender-Connectoren

- Unterstützt: Google Calendar, Outlook Calendar (weitere möglich, wenn verfügbar).
- Immer zuerst Verbindung prüfen. Bei fehlender Verbindung Connect-Karte anbieten.
- Nur auf ausdrücklichen Wunsch des Nutzers direkt eintragen. Sonst .ics liefern.

## Robustheit-Tipps

- Bei Unklarheit lieber fragen als raten.
- Name und Adresse niemals erfinden.
- Bei mehreren Aushängen den aktuellen priorisieren.

## Referenzen

- Parsing: `references/parsing-guidelines.md`
- iCal-Format und Script: `references/ical-rules.md`
- Generator: `scripts/generate_ics.py`
