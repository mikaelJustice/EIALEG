#!/usr/bin/env python3
"""
Final verification - check for any remaining blueprint-style endpoints
"""
import re
import glob

patterns_to_find = [
    r"url_for\(['\"](?:public|admin|captain|auth)\.",
    r"url_for\(\\'(?:public|admin|captain|auth)\.",
]

problem_files = []

# Check app.py
print("Checking app.py...")
try:
    with open('app.py', 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
        for pattern in patterns_to_find:
            matches = re.findall(pattern, content)
            if matches:
                problem_files.append(("app.py", len(matches)))
except Exception as e:
    print(f"Error reading app.py: {e}")

# Check all HTML template files in filesystem
print("Checking filesystem templates...")
for html_file in glob.glob('football_league_rebranded/templates/**/*.html', recursive=True):
    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()
        for pattern in patterns_to_find:
            matches = re.findall(pattern, content)
            if matches:
                problem_files.append((html_file, len(matches)))

if problem_files:
    print("\nProblems found:")
    for file, count in problem_files:
        print(f"  {file}: {count} blueprint-style references")
else:
    print("\nSUCCESS! No blueprint-style endpoints found anywhere!")
    print("All references have been successfully converted to function names.")
    print("\nReady to commit and deploy to Render.")
