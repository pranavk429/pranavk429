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

    # 2. Add entry to guestbook table
    new_entry = f'<tr><td align="center"><a href="https://github.com/{sanitized_user}"><img src="{avatar_url}&s=40" width="36px;" style="border-radius:50%;" alt="@{sanitized_user}"/><br /><sub><b>{sanitized_user}</b></sub></a></td><td>{sanitized_msg}</td></tr>'

    guestbook_pattern = r'(<!-- CAMPFIRE_GUESTBOOK:START -->\s*<table>)([\s\S]*?)(</table>\s*<!-- CAMPFIRE_GUESTBOOK:END -->)'
    match = re.search(guestbook_pattern, content)
    if match:
        prefix = match.group(1)
        existing = match.group(2).strip()
        suffix = match.group(3)
        
        # Parse existing rows
        rows = [r.strip() for r in existing.split('</tr>') if '<tr>' in r]
        rows = [r + '</tr>' for r in rows]
        rows.insert(0, new_entry)
        rows = rows[:10] # Keep last 10 entries
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
