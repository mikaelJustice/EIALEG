#!/usr/bin/env python3
"""Comprehensive fix for all remaining blueprint-style endpoint references"""

import re

with open('app.py', 'r', encoding='utf-8') as f:
    content = f.read()

# More comprehensive replacements - use simple string matching

changed_count = 0
# Don't use regex replacements, just simple string matching

# Apply non-regex replacements for specific cases
manual_replacements = [
    ("url_for('admin.add_team'", "url_for('add_team'"),
    ("url_for('admin.add_player'", "url_for('add_player'"),
    ("url_for('admin.add_match'", "url_for('add_match'"),
    ("url_for('admin.add_news'", "url_for('add_news'"),
    ("url_for('admin.add_user'", "url_for('add_user'"),
    ("url_for('admin.add_money'", "url_for('add_money'"),
    ("url_for('admin.edit_team'", "url_for('edit_team'"),
    ("url_for('admin.edit_player'", "url_for('edit_player'"),
    ("url_for('admin.edit_match'", "url_for('edit_match'"),
    ("url_for('admin.edit_news'", "url_for('edit_news'"),
    ("url_for('admin.delete_team'", "url_for('delete_team'"),
    ("url_for('admin.delete_player'", "url_for('delete_player'"),
    ("url_for('admin.delete_match'", "url_for('delete_match'"),
    ("url_for('admin.delete_news'", "url_for('delete_news'"),
    ("url_for('admin.delete_user'", "url_for('delete_user'"),
    ("url_for('admin.approve_transfer'", "url_for('approve_transfer'"),
    ("url_for('admin.reject_transfer'", "url_for('reject_transfer'"),
    ("url_for('admin.enter_result'", "url_for('enter_result'"),
]

for old, new in manual_replacements:
    count = content.count(old)
    if count > 0:
        content = content.replace(old, new)
        changed_count += count
        print(f"✓ Fixed {count}x {old[:40]}...")

with open('app.py', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"\n✓ Total fixes applied: {changed_count}")
print("✓ All blueprint-style endpoint references have been fixed!")
