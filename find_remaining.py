#!/usr/bin/env python3
import re

with open('app.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Find all remaining blueprint-style references
patterns = [
    r"url_for\(['\"]admin\.[a-z_]+['\"]",
    r"url_for\(['\"]public\.[a-z_]+['\"]",
    r"url_for\(['\"]captain\.[a-z_]+['\"]",
    r"url_for\(['\"]auth\.[a-z_]+['\"]",
]

found_any = False
for pattern in patterns:
    matches = re.findall(pattern, content)
    if matches:
        found_any = True
        for m in sorted(set(matches)):
            print(f"Found: {m}")

if not found_any:
    print("✓ No blueprint-style endpoint references found!")
else:
    print(f"\n✗ Found {len(set(m for p in patterns for m in re.findall(p, content)))} remaining references to fix")
