#!/usr/bin/env python3
"""
Quick fix script to replace blueprint-style captain endpoints in app.py TEMPLATES dictionary
"""
import re

# Read the file
with open('app.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Track replacements
replacements = [
    (r"url_for\(\\'captain\.upload_player_photo\\'", "url_for(\\'upload_player_photo\\'"),
    (r"url_for\(\\'captain\.set_price\\'", "url_for(\\'set_price\\'"),
    (r"url_for\(\\'captain\.request_transfer\\'", "url_for(\\'request_transfer\\'"),
]

original_content = content
for old_pattern, new_pattern in replacements:
    count = len(re.findall(old_pattern, content))
    if count > 0:
        content = re.sub(old_pattern, new_pattern, content)
        print(f"✓ Fixed: {old_pattern} → {new_pattern} ({count} occurrence{'s' if count > 1 else ''})")
    else:
        print(f"✗ Not found: {old_pattern}")

# Write back
if content != original_content:
    with open('app.py', 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"\n✅ File updated successfully!")
else:
    print(f"\n⚠️  No changes made - pattern not found in file")
