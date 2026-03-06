#!/usr/bin/env python3

import re

file_path = 'app.py'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Define all replacements
replacements = [
    # public.* endpoints
    (r"url_for\('public\.home'", "url_for('home'"),
    (r"url_for\('public\.league_table'", "url_for('league_table'"),
    (r"url_for\('public\.table'", "url_for('league_table'"),
    (r"url_for\('public\.fixtures'", "url_for('fixtures'"),
    (r"url_for\('public\.results'", "url_for('results'"),
    (r"url_for\('public\.teams'", "url_for('teams'"),
    (r"url_for\('public\.team_detail'", "url_for('team_detail'"),
    (r"url_for\('public\.news'", "url_for('news'"),
    (r"url_for\('public\.news_detail'", "url_for('news_detail'"),
    (r"url_for\('public\.scorers'", "url_for('scorers'"),
    
    # admin.* endpoints
    (r"url_for\('admin\.dashboard'", "url_for('admin_dashboard'"),
    (r"url_for\('admin\.teams'", "url_for('admin_teams'"),
    (r"url_for\('admin\.players'", "url_for('admin_players'"),
    (r"url_for\('admin\.matches'", "url_for('admin_matches'"),
    (r"url_for\('admin\.enter_result'", "url_for('enter_result'"),
    (r"url_for\('admin\.add_match'", "url_for('add_match'"),
    (r"url_for\('admin\.edit_match'", "url_for('edit_match'"),
    (r"url_for\('admin\.delete_match'", "url_for('delete_match'"),
    (r"url_for\('admin\.add_team'", "url_for('add_team'"),
    (r"url_for\('admin\.edit_team'", "url_for('edit_team'"),
    (r"url_for\('admin\.delete_team'", "url_for('delete_team'"),
    (r"url_for\('admin\.add_player'", "url_for('add_player'"),
    (r"url_for\('admin\.edit_player'", "url_for('edit_player'"),
    (r"url_for\('admin\.delete_player'", "url_for('delete_player'"),
    (r"url_for\('admin\.transfers'", "url_for('admin_transfers'"),
    (r"url_for\('admin\.approve_transfer'", "url_for('approve_transfer'"),
    (r"url_for\('admin\.reject_transfer'", "url_for('reject_transfer'"),
    (r"url_for\('admin\.news'", "url_for('admin_news'"),
    (r"url_for\('admin\.add_news'", "url_for('add_news'"),
    (r"url_for\('admin\.edit_news'", "url_for('edit_news'"),
    (r"url_for\('admin\.delete_news'", "url_for('delete_news'"),
    (r"url_for\('admin\.users'", "url_for('admin_users'"),
    (r"url_for\('admin\.add_user'", "url_for('add_user'"),
    (r"url_for\('admin\.delete_user'", "url_for('delete_user'"),
    (r"url_for\('admin\.add_money'", "url_for('add_money'"),
    
    # captain.* endpoints
    (r"url_for\('captain\.dashboard'", "url_for('dashboard'"),
    (r"url_for\('captain\.squad'", "url_for('squad'"),
    (r"url_for\('captain\.transfers'", "url_for('captain_transfers'"),
    (r"url_for\('captain\.lineups'", "url_for('lineups'"),
    
    # auth.* endpoints
    (r"url_for\('auth\.login'", "url_for('login'"),
    (r"url_for\('auth\.logout'", "url_for('logout'"),
]

count = 0
for pattern, replacement in replacements:
    new_content, num_subs = re.subn(pattern, replacement, content)
    if num_subs > 0:
        count += num_subs
        content = new_content
        print(f"✓ Replaced {num_subs}: {pattern} → {replacement}")

if count > 0:
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"\n✅ Total replacements: {count}")
    print(f"✅ File saved: {file_path}")
else:
    print("ℹ️  No replacements needed")
