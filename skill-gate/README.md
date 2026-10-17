# skill-gate

Lightweight two-stage security gate for loading third-party AI skills.

This skill acts as an always-on interceptor. Whenever you ask an agent to load, install, or activate another skill, it first performs a static review of the target skill’s files before any of its instructions are followed.

## What it does

- **Stage 1 (fast path):** Quick static checks on `SKILL.md` and all accompanying files. Looks for description vs body mismatch, obvious red-flag patterns, sandbox vs host signals, data-scope issues (local vs persistent identity files), basic dangerous code patterns, and prohibited intent.
- **Stage 2 (optional, only on grey area):** Deeper static analysis plus comparison against known public threat lists and reports (e.g. Snyk ToxicSkills, OWASP Agentic Skills case studies). Only runs if you explicitly confirm.
- Never executes the target skill.
- Prefers speed: clean skills should clear Stage 1 in seconds.
- Explicitly allows harsh criticism, devil’s advocate, and red-teaming.
- Flags actionable assistance for severe real-world harm and emotional manipulation aimed at extracting money, credentials, or sustained dependency.

Possible outcomes after Stage 1:
- **OK** — Skill looks fine. Asks whether you want to install and continue.
- **Red Flag** — Stops immediately and lists the critical findings.
- **Grey Area** — Offers to continue with Stage 2.

## Installation

### Recommended: Ask the agent (copy-paste)

Copy the following message into your chat:

```
Install the skill-gate skill from https://github.com/iNand/personal-ai-skills/tree/main/skill-gate
```

### Alternative 1: Download ZIP

1. Download the repository as ZIP:  
   https://github.com/iNand/personal-ai-skills/archive/refs/heads/main.zip
2. Extract it.
3. Upload or point the agent to the extracted `skill-gate` folder and say:

```
Install the skill from this folder
```

### Alternative 2: Copy the skill text into the chat

1. Open the raw SKILL.md:  
   https://raw.githubusercontent.com/iNand/personal-ai-skills/main/skill-gate/SKILL.md
2. Copy the entire content.
3. Paste it into the chat and say:

```
Create and install a skill from the following SKILL.md content:

[paste content here]
```

## Usage

Once installed, the gate is always active. You do not need to invoke it explicitly. Simply ask to load any other skill as usual. The gate will intercept the request, run Stage 1, and present the result before proceeding.

## Structure

```
skill-gate/
├── README.md
└── SKILL.md
```

## Notes

- Static analysis only — the target skill is never executed during the check.
- The gate treats foreign SKILL.md files as untrusted data until you confirm activation.
- For maximum protection, keep this skill loaded permanently.

## License

MIT (see repository root).
