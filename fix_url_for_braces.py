#!/usr/bin/env python3
"""Fix the malformed url_for calls that are missing closing Jinja2 braces"""
import re

with open('app.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern: {{ url_for('endpoint') without closing }} should become {{ url_for('endpoint') }}
# Looking for: {{ url_for\(\'...\')\) followed by a quote or space (not }}
pattern = r'\{\{\s*url_for\(\\'([^\']+)\\'\)(["\'])\s'
replacement = r'{{ url_for(\'\1\') }}\2 '

# Count matches
matches_before = len(re.findall(pattern, content))
print(f"Found {matches_before} missing closing }} in url_for calls")

if matches_before > 0:
    # Apply fix
    fixed_content = re.sub(pattern, replacement, content)
    
    # Write back
    with open('app.py', 'w', encoding='utf-8') as f:
        f.write(fixed_content)
    
    print(f"✓ Fixed all {matches_before} url_for calls with missing closing }}")
else:
    # Try a different approach - look for {{ url_for without }}
    pattern2 = r'\{\{\s*url_for\(\\'([^\']+)\\'\)\)([^}])'
    matches_before2 = len(re.findall(pattern2, content))
    print(f"Found {matches_before2} with alternate pattern")
    
    if matches_before2 > 0:
        replacement2 = r'{{ url_for(\'\1\') }}\2'
        fixed_content = re.sub(pattern2, replacement2, content)
        with open('app.py', 'w', encoding='utf-8') as f:
            f.write(fixed_content)
        print(f"✓ Fixed all {matches_before2} url_for calls with alternate pattern")
