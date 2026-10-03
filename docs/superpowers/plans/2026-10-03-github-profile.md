# GitHub Profile ("The Agent Outpost") Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a retro pixel campfire GitHub profile README for @pranavk429 featuring an interactive automated guestbook, telemetry HUD, and system showcase.

**Architecture:** A GitHub profile repository (`pranavk429/pranavk429`) housing a rich `README.md`, assets, an interactive campfire guestbook powered by GitHub Actions (`.github/workflows/campfire-guestbook.yml`), and a deterministic Python parsing script with test coverage.

**Tech Stack:** Markdown, SVG (`readme-typing-svg`), GitHub Actions, Python 3, Pytest.

---

### Task 1: Assets and Test-Driven Interactive Guestbook Script

**Files:**
- Create: `scripts/add_guestbook_entry.py`
- Create: `tests/test_guestbook.py`

- [ ] **Step 1: Write unit tests for guestbook parser and updater**

```python
import pytest
from scripts.add_guestbook_entry import sanitize_message, update_readme_content

def test_sanitize_message():
    assert sanitize_message("Hello from the outpost! <script>alert(1)</script>") == "Hello from the outpost! alert(1)"
    assert sanitize_message("A" * 150) == "A" * 80 + "..."
    assert sanitize_message("") == "Stopped by the campfire."

def test_update_readme_content():
    initial_readme = """
# Header
<!-- CAMPFIRE_COUNT:START -->1<!-- CAMPFIRE_COUNT:END --> logs burning
<!-- CAMPFIRE_GUESTBOOK:START -->
- [pranavk429](https://github.com/pranavk429): Ignited the campfire flame.
<!-- CAMPFIRE_GUESTBOOK:END -->
## Footer
"""
    updated = update_readme_content(
        initial_readme,
        username="octocat",
        message="Brought some dry firewood!",
        avatar_url="https://github.com/octocat.png"
    )
    assert "<!-- CAMPFIRE_COUNT:START -->2<!-- CAMPFIRE_COUNT:END -->" in updated
    assert "octocat" in updated
    assert "Brought some dry firewood!" in updated
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_guestbook.py`
Expected: FAIL (module not found)

- [ ] **Step 3: Implement `scripts/add_guestbook_entry.py`**

```python
import re
import html
import sys

def sanitize_message(raw_msg: str, max_len: int = 80) -> str:
    if not raw_msg or not raw_msg.strip():
        return "Stopped by the campfire."
    cleaned = re.sub(r'<[^>]*>', '', raw_msg)
    cleaned = html.escape(cleaned.strip())
    if len(cleaned) > max_len:
        cleaned = cleaned[:max_len] + "..."
    return cleaned

def update_readme_content(content: str, username: str, message: str, avatar_url: str = "") -> str:
    sanitized_msg = sanitize_message(message)
    sanitized_user = re.sub(r'[^a-zA-Z0-9_\-]', '', username)
    if not avatar_url:
        avatar_url = f"https://github.com/{sanitized_user}.png"

    # 1. Update count
    count_match = re.search(r'<!-- CAMPFIRE_COUNT:START -->(\d+)<!-- CAMPFIRE_COUNT:END -->', content)
    current_count = int(count_match.group(1)) if count_match else 1
    new_count = current_count + 1
    content = re.sub(
        r'<!-- CAMPFIRE_COUNT:START -->\d+<!-- CAMPFIRE_COUNT:END -->',
        f'<!-- CAMPFIRE_COUNT:START -->{new_count}<!-- CAMPFIRE_COUNT:END -->',
        content
    )

    # 2. Add entry to guestbook
    new_entry = f'<tr><td align="center"><a href="https://github.com/{sanitized_user}"><img src="{avatar_url}&s=40" width="36px;" style="border-radius:50%;" alt="@{sanitized_user}"/><br /><sub><b>{sanitized_user}</b></sub></a></td><td>{sanitized_msg}</td></tr>'

    # Check for table or list format
    guestbook_pattern = r'(<!-- CAMPFIRE_GUESTBOOK:START -->\s*(?:<table>)?)([\s\S]*?)((?:</table>)?\s*<!-- CAMPFIRE_GUESTBOOK:END -->)'
    match = re.search(guestbook_pattern, content)
    if match:
        prefix = match.group(1)
        existing = match.group(2).strip()
        suffix = match.group(3)
        if not prefix.endswith('<table>\n'):
            prefix = '<!-- CAMPFIRE_GUESTBOOK:START -->\n<table>\n'
            suffix = '\n</table>\n<!-- CAMPFIRE_GUESTBOOK:END -->'
        
        # Keep last 8 entries
        rows = [r.strip() for r in existing.split('</tr>') if '<tr>' in r]
        rows = [r + '</tr>' for r in rows]
        rows.insert(0, new_entry)
        rows = rows[:8]
        updated_block = f"{prefix}\n" + "\n".join(rows) + f"\n{suffix}"
        content = content[:match.start()] + updated_block + content[match.end():]

    return content

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python add_guestbook_entry.py <username> <message> [avatar_url]")
        sys.exit(1)
    user = sys.argv[1]
    msg = sys.argv[2]
    avatar = sys.argv[3] if len(sys.argv) > 3 else ""
    with open("README.md", "r", encoding="utf-8") as f:
        readme = f.read()
    new_readme = update_readme_content(readme, user, msg, avatar)
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(new_readme)
    print(f"Successfully added guestbook entry for {user}")
```

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest tests/test_guestbook.py`
Expected: PASS

---

### Task 2: Build the Production README.md

**Files:**
- Create: `README.md`

- [ ] **Step 1: Write `README.md` with full campfire styling, typing header, terminal telemetry, systems showcase, and guestbook markers**

Include:
- Campfire banner image (`assets/banner.jpg`)
- Animated Typing SVG
- Terminal Box with ASCII borders
- Systems Grid Cards with badges (Ark-Agents, Tower-Trace, Argus, Coral-Reef, Echo)
- Interactive Campfire Guestbook with issue template link
- Synthwave styled GitHub Readme Stats cards

---

### Task 3: Setup GitHub Action & Issue Template for Guestbook

**Files:**
- Create: `.github/workflows/campfire-guestbook.yml`
- Create: `.github/ISSUE_TEMPLATE/campfire-log.yml`

- [ ] **Step 1: Create structured issue template**
- [ ] **Step 2: Create GitHub Action workflow that runs on issue open, calls `scripts/add_guestbook_entry.py`, commits to main, and closes the issue**

---

### Task 4: Interactive Local Preview & Validation Gate

**Files:**
- Create: `preview.html` (Local preview of the exact markdown rendering)

- [ ] **Step 1: Verify all unit tests pass**
- [ ] **Step 2: Serve local preview for user inspection**
- [ ] **Step 3: Pause for user reconfirmation before any remote repository push**
