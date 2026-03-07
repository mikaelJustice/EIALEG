#!/usr/bin/env python3
"""Fix all malformed url_for calls missing closing parenthesis"""
import re

with open('app.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern: url_for('endpoint' }} should be url_for('endpoint')
# In the actual file it's: url_for(\'endpoint\' }}
pattern1 = r"url_for\(\\'([^']+)\\'\s\}\}"
replacement1 = r"url_for('\1')"

# Count matches before
matches_before = len(re.findall(pattern1, content))
print(f"Found {matches_before} malformed url_for calls with pattern: url_for('endpoint' }}")

# Apply fix
fixed_content = re.sub(pattern1, replacement1, content)

# Verify
matches_after = len(re.findall(pattern1, fixed_content))
print(f"After fix: {matches_after} remaining")

if matches_before > 0 and matches_after == 0:
    with open('app.py', 'w', encoding='utf-8') as f:
        f.write(fixed_content)
    print(f"✓ Successfully fixed {matches_before} url_for calls")
elif matches_before == 0:
    print("No malformed url_for calls found")
else:
    print(f"Warning: Still {matches_after} malformed calls remaining after fix")
