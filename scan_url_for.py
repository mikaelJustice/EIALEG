#!/usr/bin/env python3
"""Find all url_for calls that don't have proper closing}}"""
import re

with open('app.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Look for {{ url_for(...) }} pattern
# Count all url_for calls and see which ones are missing }}
pattern_correct = r'\{\{\s*url_for\([^)]+\)\s*\}\}'
pattern_broken = r'\{\{\s*url_for\([^)]+\)\s["\']'

correct_matches = len(re.findall(pattern_correct, content))
broken_matches = len(re.findall(pattern_broken, content))

print(f"Correct url_for calls with }}: {correct_matches}")
print(f"Broken url_for calls missing }}: {broken_matches}")

# Show some examples of broken ones
broken_pattern = r'\{\{\s*url_for\([^)]+\)(?=["\'])'
broken_examples = re.findall(broken_pattern, content)
if broken_examples:
    print(f"\nFirst few broken examples:")
    for i, example in enumerate(broken_examples[:3]):
        print(f"  {i+1}: {example}")
