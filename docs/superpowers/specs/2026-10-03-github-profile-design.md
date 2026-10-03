# Specification: pranavk429 GitHub Profile ("The Agent Outpost")

## Overview
A distinctive, high-craft GitHub profile README and interactive visitor guestbook for `@pranavk429`. 
The profile blends the developer's 16-bit campfire avatar and deep expertise in AI agent engineering, policy gateways, and causal SRE systems.

## Design Goals
1. **Aesthetic Cohesion**: Visual language rooted in 16-bit retro campfire pixel art, twilight purple/indigo hues, ember orange, and neon cyan accents matching the user's avatar.
2. **Technical Depth**: Highlights high-value repositories (`Ark-Agents`, `Tower-Trace`, `Argus`, `coral-reef`, `echo`) with crisp architecture summaries and badge pills.
3. **Interactivity**: An automated GitHub Actions guestbook ("Campfire Outpost") where visitors can click an issue link to throw wood on the campfire, updating the README in real time with their avatar and message.
4. **Telemetry**: Dynamic GitHub stats and top languages cards styled in a matching custom synthwave/campfire theme.

## Architecture

### File Layout
```
pranavk429/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   └── campfire-log.yml         # Structured issue template for guestbook
│   └── workflows/
│       └── campfire-guestbook.yml   # GitHub Action triggering on guestbook issues
├── assets/
│   └── banner.jpg                   # 16-bit pixel art campfire banner (high-res)
├── scripts/
│   └── add_guestbook_entry.py       # Deterministic Python parser & README updater
├── tests/
│   └── test_guestbook.py            # Unit test suite verifying sanitization & regex
├── docs/
│   └── superpowers/
│       ├── specs/
│       │   └── 2026-10-03-github-profile-design.md
│       └── plans/
│           └── 2026-10-03-github-profile.md
└── README.md                        # The profile README rendered by GitHub
```

### Components
1. **Hero Banner**:
   - `assets/banner.jpg`: 16-bit pixel art campfire scene under starry night sky.
   - Animated typing SVG headline (`readme-typing-svg`):
     - `> Architecting deterministic agent kernels`
     - `> Building fail-closed policy gateways & causal SRE`
     - `> Exploring multi-agent consensus & NPC memory systems`
2. **Agent Telemetry Console**:
   - Monospaced ASCII box detailing runtime state, mission directive, active agents, and core tech toolkit.
3. **Featured Systems Showcase**:
   - Grid cards for `Ark-Agents`, `Tower-Trace`, `Argus`, `coral-reef`, and `echo`.
4. **Interactive Campfire Guestbook**:
   - Counter tracking total logs added.
   - Avatars and messages of travelers who visited.
   - Pre-formatted issue link: `[🔥 Add Wood to the Campfire / Sign Outpost Log]`.
5. **System Telemetry & Activity**:
   - GitHub stats card + Top languages card using custom hex query params:
     - `bg_color=0d1117`
     - `title_color=00f5d4`
     - `text_color=e6edf3`
     - `border_color=ff6b35`
     - `icon_color=ff6b35`
