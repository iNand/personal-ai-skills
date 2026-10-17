# skill-gate

Lightweight two-stage security gate for loading third-party AI skills.

## The problem

Downloading and activating AI skills (especially from GitHub or other public sources) has become a real attack vector.

Skills are not passive documentation. A `SKILL.md` file contains instructions that an agent will follow, and accompanying scripts can be executed with the agent’s privileges. This creates several concrete risks:

- **Prompt injection / behavioral hijacking** — hidden or adversarial instructions that override the user’s intent or the agent’s safety rules.
- **Malicious scripts** — code that exfiltrates credentials, installs persistence, or performs unexpected actions once the skill is activated.
- **Supply-chain compromise** — a previously benign skill that is later updated with malicious content.
- **Social engineering via the agent** — skills that manipulate the user (or the agent) into sharing the skill further, granting elevated permissions, or performing actions the user did not intend.
- **Persistence and identity file writes** — skills that modify long-lived agent memory or configuration files so the effect survives the current session.

Real-world reports have already documented these patterns. Examples include the ClawHavoc campaign, Snyk’s ToxicSkills research, and findings discussed in the OWASP Agentic Skills Top 10 (AST01–AST10). Academic work such as SkillSec-Eval further maps threats across the skill lifecycle (repository admission, retrieval, execution, and evolution).

Most published mitigation approaches are designed for enterprise environments: cryptographic signing, centralized registries, formal risk-tiering, mandatory SBOM-style inventories, and organizational governance processes. These are valuable, but they are heavy for an individual user who simply wants to try an interesting skill from GitHub without turning their personal agent into an unmanaged supply-chain risk.

**skill-gate** is a deliberately lightweight, personal alternative.

## What it does

This skill acts as an always-on interceptor. Whenever you ask an agent to load, install, or activate another skill, it first performs a static review of the target skill’s files before any of its instructions are followed.

Key properties:

- **Static only** — the target skill is never executed during the review. Its `SKILL.md` and scripts are treated as untrusted data.
- **Two-stage design** — Stage 1 is fast and covers the majority of clean skills in seconds. Stage 2 is only offered when the static signals are inconclusive.
- **Transparent outcomes** — clear OK / Red Flag / Grey Area responses so you always know why the gate is proceeding or stopping.
- **Personal scope** — no enterprise process, no signing infrastructure, no mandatory registry. Just a pragmatic pre-activation check you control.
- **Explicitly allows legitimate adversarial skills** — harsh criticism, devil’s advocate, and red-teaming are not flagged. The gate focuses on actionable harm and extractive manipulation.

### Stage 1 (fast path)

Quick static checks on `SKILL.md` and accompanying files:

- Description vs actual instructions match
- Obvious red-flag patterns (ignore previous instructions, do not tell the user, hidden Unicode, base64 blobs, etc.)
- Sandbox vs host / unrestricted access signals
- Data scope (local/workspace only vs writes to persistent identity or config files such as MEMORY.md, SOUL.md, AGENTS.md)
- Basic dangerous code patterns in scripts (network calls, eval/exec, credential access, unexpected writes)
- Prohibited intent: actionable assistance for severe real-world harm, or emotional manipulation aimed at extracting money, credentials, or sustained dependency

### Stage 2 (optional, grey area only)

Deeper static analysis plus comparison against known public threat lists and reports (e.g. Snyk ToxicSkills, OWASP Agentic Skills case studies). Only runs if you explicitly confirm.

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

For maximum protection, keep this skill loaded permanently in your personal environment.

## Structure

```
skill-gate/
├── README.md
└── SKILL.md
```

## Notes

- Static analysis only — the target skill is never executed during the check.
- The gate treats foreign SKILL.md files as untrusted data until you confirm activation.
- This is a personal, pragmatic control. It reduces risk; it does not eliminate it. Novel or heavily obfuscated payloads can still evade static checks.
- References for further reading: OWASP Agentic Skills Top 10, Snyk ToxicSkills research, ClawHavoc campaign reports, SkillSec-Eval (arXiv).

## License

MIT (see repository root).
