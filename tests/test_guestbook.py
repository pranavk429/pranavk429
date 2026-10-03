import unittest
import os
import sys

# Ensure scripts dir is on sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scripts.add_guestbook_entry import sanitize_message, update_readme_content

class TestGuestbook(unittest.TestCase):
    def test_sanitize_message_strips_html(self):
        raw = "Hello from the outpost! <script>alert(1)</script>"
        clean = sanitize_message(raw)
        self.assertNotIn("<script>", clean)
        self.assertIn("alert(1)", clean)

    def test_sanitize_message_truncates_long_inputs(self):
        long_msg = "A" * 150
        clean = sanitize_message(long_msg, max_len=80)
        self.assertLessEqual(len(clean), 85)
        self.assertTrue(clean.endswith("..."))

    def test_sanitize_message_handles_empty(self):
        self.assertEqual(sanitize_message(""), "Stopped by the campfire.")
        self.assertEqual(sanitize_message("   "), "Stopped by the campfire.")

    def test_update_readme_content(self):
        initial_readme = """# Campfire
<!-- CAMPFIRE_COUNT:START -->1<!-- CAMPFIRE_COUNT:END --> logs burning

<!-- CAMPFIRE_GUESTBOOK:START -->
<table>
<tr><td align="center"><a href="https://github.com/pranavk429"><img src="https://github.com/pranavk429.png&s=40" width="36px;" style="border-radius:50%;" alt="@pranavk429"/><br /><sub><b>pranavk429</b></sub></a></td><td>Ignited the campfire flame.</td></tr>
</table>
<!-- CAMPFIRE_GUESTBOOK:END -->
"""
        updated = update_readme_content(
            initial_readme,
            username="octocat",
            message="Brought some dry firewood!",
            avatar_url="https://github.com/octocat.png"
        )
        self.assertIn("<!-- CAMPFIRE_COUNT:START -->2<!-- CAMPFIRE_COUNT:END -->", updated)
        self.assertIn("octocat", updated)
        self.assertIn("Brought some dry firewood!", updated)

if __name__ == "__main__":
    unittest.main()
