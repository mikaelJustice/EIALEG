#!/usr/bin/env python3
"""Fix the malformed url_for calls that are missing closing Jinja2 braces"""
import re

with open('app.py', 'r', encoding='utf-8') as f:
    content = f.read()

# The pattern should be: url_for('endpoint' }} should become url_for('endpoint') }}
# In escaped form: url_for(\'endpoint\' }} should become url_for(\'endpoint\') }}
pattern = r"url_for\(\\'([^']+)\\'\s\}\}"
replacement = r"url_for('\1') }}"

# Count matches
matches_before = len(re.findall(pattern, content))
print(f"Found {matches_before} malformed url_for calls")

# Apply fix
fixed_content = re.sub(pattern, replacement, content)

# Verify
matches_after = len(re.findall(pattern, fixed_content))
print(f"After fix: {matches_after} remaining")

if matches_before > 0:
    with open('app.py', 'w', encoding='utf-8') as f:
        f.write(fixed_content)
    if matches_after == 0:
        print(f"✓ Successfully fixed all {matches_before} url_for calls")
    else:
        print(f"Warning: {matches_after} malformed calls still remaining")
else:
    print("No malformed url_for calls found")
