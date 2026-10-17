# skill-gate

Lightweight two-stage security gate for loading third-party AI skills.

## What it does

Intercepts any request to load, install, or activate a skill and performs a static-only review before any of its instructions are followed.

- **Stage 1 (fast path):** Quick static checks on `SKILL.md` and accompanying files (description match, obvious red flags, sandbox vs host signals, data scope, basic code patterns, prohibited intent).
- **Stage 2 (optional):** Deeper static analysis and comparison against known public threat lists — only if Stage 1 is inconclusive and you confirm.

Never executes the target skill. Prefers speed for clean skills.

## Installation

Ask the agent to install the skill (e.g. “Install the skill-gate skill from this repo” or point it at the folder / GitHub URL).

## Usage

Once installed, the gate is always active. Any time you ask to load another skill, it runs automatically and returns one of:

- **OK** — “Skill looks okay… Do you want to install and continue?”
- **Red Flag** — stops immediately with findings.
- **Grey Area** — offers Stage 2 for a deeper review.

## Structure

```
skill-gate/
└── SKILL.md
```

## Notes

- Static analysis only — the target skill is never executed.
- Explicitly allows harsh criticism, devil’s advocate, and red-teaming.
- Flags actionable help for severe real-world harm and emotional manipulation aimed at extracting money or dependency.

## License

MIT (see repository root if present).
