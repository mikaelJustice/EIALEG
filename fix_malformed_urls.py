#!/usr/bin/env python3
"""
Fix malformed url_for strings left by previous regex replacements
"""
import os

os.chdir(r'c:\Users\FML\Desktop\football_league_rebranded\EIALEG')

with open('app.py', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

# Find and fix malformed patterns like:  url_for('dashboard' }}"
# These should be: url_for('dashboard') }}

problem_patterns = [
    ("url_for(\\'dashboard\\' }}", "url_for(\\'dashboard\\') }}"),
    ("url_for(\\'transfers\\' }}", "url_for(\\'transfers\\') }}"),
    ("url_for(\\'lineups\\' }}", "url_for(\\'lineups\\') }}"),
    ("url_for(\\'captain.submit_lineup\\'", "url_for(\\'submit_lineup\\'"),
    #Add any other malformed patterns here
]

original = content
for old, new in problem_patterns:
    content = content.replace(old, new)

# Also check for patterns without proper closing quote
changes_made = original != content

if changes_made:
    with open('app.py', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Fixed malformed url_for patterns in app.py")
    
    # Verify
    broken_count = content.count("{{'") + content.count("url_for(\\'dashboard\\' }}")
    print(f"Remaining potential issues: {broken_count}")
else:
    print("No malformed patterns found")
