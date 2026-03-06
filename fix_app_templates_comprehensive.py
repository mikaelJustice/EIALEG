#!/usr/bin/env python3
"""
Comprehensive fix for all blueprint-style endpoints in app.py including those with parameters
"""
import re
import os

os.chdir(r'c:\Users\FML\Desktop\football_league_rebranded\EIALEG')

with open('app.py', 'r', encoding='utf-8') as f:
    content = f.read()

original_content = content

# Define replacement pairs - these handle both with and without parameters
pattern_replacements = [
    # Admin patterns (with or without parameters)
    (r"url_for\(\\'admin\.dashboard\\'", r"url_for(\\'admin_dashboard\\'"),
    (r"url_for\(\\'admin\.teams\\'", r"url_for(\\'admin_teams\\'"),
    (r"url_for\(\\'admin\.players\\'", r"url_for(\\'admin_players\\'"),
    (r"url_for\(\\'admin\.matches\\'", r"url_for(\\'admin_matches\\'"),
    (r"url_for\(\\'admin\.transfers\\'", r"url_for(\\'admin_transfers\\'"),
    (r"url_for\(\\'admin\.news\\'", r"url_for(\\'admin_news\\'"),
    (r"url_for\(\\'admin\.users\\'", r"url_for(\\'admin_users\\'"),
    (r"url_for\(\\'admin\.add_team\\'", r"url_for(\\'add_team\\'"),
    (r"url_for\(\\'admin\.add_player\\'", r"url_for(\\'add_player\\'"),
    (r"url_for\(\\'admin\.add_match\\'", r"url_for(\\'add_match\\'"),
    (r"url_for\(\\'admin\.add_news\\'", r"url_for(\\'add_news\\'"),
    (r"url_for\(\\'admin\.add_user\\'", r"url_for(\\'add_user\\'"),
    (r"url_for\(\\'admin\.add_money\\'", r"url_for(\\'add_money\\'"),
    (r"url_for\(\\'admin\.edit_team\\'", r"url_for(\\'edit_team\\'"),
    (r"url_for\(\\'admin\.edit_player\\'", r"url_for(\\'edit_player\\'"),
    (r"url_for\(\\'admin\.edit_match\\'", r"url_for(\\'edit_match\\'"),
    (r"url_for\(\\'admin\.edit_news\\'", r"url_for(\\'edit_news\\'"),
    (r"url_for\(\\'admin\.delete_team\\'", r"url_for(\\'delete_team\\'"),
    (r"url_for\(\\'admin\.delete_player\\'", r"url_for(\\'delete_player\\'"),
    (r"url_for\(\\'admin\.delete_match\\'", r"url_for(\\'delete_match\\'"),
    (r"url_for\(\\'admin\.delete_news\\'", r"url_for(\\'delete_news\\'"),
    (r"url_for\(\\'admin\.delete_user\\'", r"url_for(\\'delete_user\\'"),
    (r"url_for\(\\'admin\.enter_result\\'", r"url_for(\\'enter_result\\'"),
    (r"url_for\(\\'admin\.approve_transfer\\'", r"url_for(\\'approve_transfer\\'"),
    (r"url_for\(\\'admin\.reject_transfer\\'", r"url_for(\\'reject_transfer\\'"),

    # Public patterns
    (r"url_for\(\\'public\.home\\'", r"url_for(\\'home\\'"),
    (r"url_for\(\\'public\.fixtures\\'", r"url_for(\\'fixtures\\'"),
    (r"url_for\(\\'public\.results\\'", r"url_for(\\'results\\'"),
    (r"url_for\(\\'public\.teams\\'", r"url_for(\\'teams\\'"),
    (r"url_for\(\\'public\.team_detail\\'", r"url_for(\\'team_detail\\'"),
    (r"url_for\(\\'public\.news\\'", r"url_for(\\'news\\'"),
    (r"url_for\(\\'public\.news_detail\\'", r"url_for(\\'news_detail\\'"),
    (r"url_for\(\\'public\.table\\'", r"url_for(\\'league_table\\'"),
    (r"url_for\(\\'public\.league_table\\'", r"url_for(\\'league_table\\'"),
    (r"url_for\(\\'public\.scorers\\'", r"url_for(\\'scorers\\'"),

    # Auth patterns
    (r"url_for\(\\'auth\.login\\'", r"url_for(\\'login\\'"),
    (r"url_for\(\\'auth\.logout\\'", r"url_for(\\'logout\\'"),

    # Captain patterns
    (r"url_for\(\\'captain\.dashboard\\'", r"url_for(\\'dashboard\\'"),
    (r"url_for\(\\'captain\.squad\\'", r"url_for(\\'squad\\'"),
    (r"url_for\(\\'captain\.transfers\\'", r"url_for(\\'transfers\\'"),
    (r"url_for\(\\'captain\.lineups\\'", r"url_for(\\'lineups\\'"),
]

# Apply all regex replacements
for pattern, replacement in pattern_replacements:
    content = re.sub(pattern, replacement, content)

# Also fix endpoint comparisons
content = content.replace("request.endpoint == \\'admin.dashboard\\'", "request.endpoint == \\'admin_dashboard\\'")
content = content.replace("'admin.dashboard' in request.endpoint", "'admin_dashboard' in request.endpoint")

if content == original_content:
    print("No changes needed")
else:
    with open('app.py', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("SUCCESS! Fixed all app.py TEMPLATES dictionary references")
    
    # Verify key changes
    verification = [
        (r"url_for\(\\'admin_dashboard\\'", "Admin dashboard refs"),
        (r"url_for\(\\'admin\.dashboard\\'", "Old admin.dashboard (should be 0)"),
        (r"url_for\(\\'public\.home\\'", "Old public.home (should be 0)"),
        (r"url_for\(\\'home\\'", "Fixed home refs"),
        (r"url_for\(\\'admin_teams\\'", "Admin teams refs"),
    ]
    
    print("\nVerification:")
    for pattern, desc in verification:
        count = len(re.findall(pattern, content))
        print(f"  {desc}: {count} matches")
