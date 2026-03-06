#!/usr/bin/env python3
"""
Fix all blueprint-style endpoints in app.py TEMPLATES dictionary
"""
import os

os.chdir(r'c:\Users\FML\Desktop\football_league_rebranded\EIALEG')

with open('app.py', 'r', encoding='utf-8') as f:
    content = f.read()

original_content = content

# All replacements for escaped quotes in TEMPLATES dictionary
replacements = [
    # Admin endpoints (escaped quotes)
    ("{{ url_for(\\'admin.dashboard\\')", "{{ url_for(\\'admin_dashboard\\'"),
    ("{{ url_for(\\'admin.teams\\')", "{{ url_for(\\'admin_teams\\'"),
    ("{{ url_for(\\'admin.players\\')", "{{ url_for(\\'admin_players\\'"),
    ("{{ url_for(\\'admin.matches\\')", "{{ url_for(\\'admin_matches\\'"),
    ("{{ url_for(\\'admin.transfers\\')", "{{ url_for(\\'admin_transfers\\'"),
    ("{{ url_for(\\'admin.news\\')", "{{ url_for(\\'admin_news\\'"),
    ("{{ url_for(\\'admin.users\\')", "{{ url_for(\\'admin_users\\'"),
    ("{{ url_for(\\'admin.add_team\\')", "{{ url_for(\\'add_team\\'"),
    ("{{ url_for(\\'admin.add_player\\')", "{{ url_for(\\'add_player\\'"),
    ("{{ url_for(\\'admin.add_match\\')", "{{ url_for(\\'add_match\\'"),
    ("{{ url_for(\\'admin.add_news\\')", "{{ url_for(\\'add_news\\'"),
    ("{{ url_for(\\'admin.add_user\\')", "{{ url_for(\\'add_user\\'"),
    ("{{ url_for(\\'admin.edit_team\\')", "{{ url_for(\\'edit_team\\'"),
    ("{{ url_for(\\'admin.edit_player\\')", "{{ url_for(\\'edit_player\\'"),
    ("{{ url_for(\\'admin.edit_match\\')", "{{ url_for(\\'edit_match\\'"),
    ("{{ url_for(\\'admin.edit_news\\')", "{{ url_for(\\'edit_news\\'"),
    ("{{ url_for(\\'admin.delete_team\\')", "{{ url_for(\\'delete_team\\'"),
    ("{{ url_for(\\'admin.delete_player\\')", "{{ url_for(\\'delete_player\\'"),
    ("{{ url_for(\\'admin.delete_match\\')", "{{ url_for(\\'delete_match\\'"),
    ("{{ url_for(\\'admin.delete_news\\')", "{{ url_for(\\'delete_news\\'"),
    ("{{ url_for(\\'admin.delete_user\\')", "{{ url_for(\\'delete_user\\'"),
    ("{{ url_for(\\'admin.enter_result\\')", "{{ url_for(\\'enter_result\\'"),
    ("{{ url_for(\\'admin.approve_transfer\\')", "{{ url_for(\\'approve_transfer\\'"),
    ("{{ url_for(\\'admin.reject_transfer\\')", "{{ url_for(\\'reject_transfer\\'"),

    # Public endpoints (escaped quotes)
    ("{{ url_for(\\'public.home\\')", "{{ url_for(\\'home\\'"),
    ("{{ url_for(\\'public.fixtures\\')", "{{ url_for(\\'fixtures\\'"),
    ("{{ url_for(\\'public.results\\')", "{{ url_for(\\'results\\'"),
    ("{{ url_for(\\'public.teams\\')", "{{ url_for(\\'teams\\'"),
    ("{{ url_for(\\'public.team_detail\\')", "{{ url_for(\\'team_detail\\'"),
    ("{{ url_for(\\'public.news\\')", "{{ url_for(\\'news\\'"),
    ("{{ url_for(\\'public.news_detail\\')", "{{ url_for(\\'news_detail\\'"),
    ("{{ url_for(\\'public.table\\')", "{{ url_for(\\'league_table\\'"),
    ("{{ url_for(\\'public.league_table\\')", "{{ url_for(\\'league_table\\'"),
    ("{{ url_for(\\'public.scorers\\')", "{{ url_for(\\'scorers\\'"),

    # Auth endpoints (escaped quotes)
    ("{{ url_for(\\'auth.login\\')", "{{ url_for(\\'login\\'"),
    ("{{ url_for(\\'auth.logout\\')", "{{ url_for(\\'logout\\'"),

    # Captain endpoints (escaped quotes)
    ("{{ url_for(\\'captain.dashboard\\')", "{{ url_for(\\'dashboard\\'"),
    ("{{ url_for(\\'captain.squad\\')", "{{ url_for(\\'squad\\'"),
    ("{{ url_for(\\'captain.transfers\\')", "{{ url_for(\\'transfers\\'"),
    ("{{ url_for(\\'captain.lineups\\')", "{{ url_for(\\'lineups\\'"),
    
    # request.endpoint comparisons 
    ("request.endpoint == \\'admin.dashboard\\'", "request.endpoint == \\'admin_dashboard\\'"),
    ("'admin.dashboard' in request.endpoint", "'admin_dashboard' in request.endpoint"),
]

# Apply all replacements
for old, new in replacements:
    content = content.replace(old, new)

if content == original_content:
    print("No changes needed")
else:
    # Count changes
    changes = sum(1 for old, new in replacements if content.count(new) > original_content.count(new))
    
    with open('app.py', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("SUCCESS! Fixed app.py TEMPLATES dictionary")
    print(f"Total replacement patterns applied: {len(replacements)}")
    
    # Verify some key changes
    verification = [
        ("{{ url_for(\\'admin_dashboard\\'", "Admin dashboard link"),
        ("{{ url_for(\\'public.home\\'", "Blueprint home (should be 0)"),
        ("{{ url_for(\\'home\\'", "Function home"),
        ("{{ url_for(\\'admin_teams\\'", "Admin teams"),
    ]
    
    print("\nVerification:")
    for pattern, desc in verification:
        count = content.count(pattern)
        print(f"  {desc}: {count} matches")
