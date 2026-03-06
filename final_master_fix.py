#!/usr/bin/env python3
"""
Final master fix - handles all blueprint-style URLs including those with parameters
"""
import os
import glob

os.chdir(r'c:\Users\FML\Desktop\football_league_rebranded\EIALEG')

REPLACEMENTS = [
    # Admin blueprint replacements (with and without parameters)
    ("url_for('admin.dashboard'", "url_for('admin_dashboard'"),
    ("url_for('admin.teams'", "url_for('admin_teams'"),
    ("url_for('admin.players'", "url_for('admin_players'"),
    ("url_for('admin.matches'", "url_for('admin_matches'"),
    ("url_for('admin.transfers'", "url_for('admin_transfers'"),
    ("url_for('admin.news'", "url_for('admin_news'"),
    ("url_for('admin.users'", "url_for('admin_users'"),
    ("url_for('admin.add_team'", "url_for('add_team'"),
    ("url_for('admin.add_player'", "url_for('add_player'"),
    ("url_for('admin.add_match'", "url_for('add_match'"),
    ("url_for('admin.add_news'", "url_for('add_news'"),
    ("url_for('admin.add_user'", "url_for('add_user'"),
    ("url_for('admin.add_money'", "url_for('add_money'"),
    ("url_for('admin.edit_team'", "url_for('edit_team'"),
    ("url_for('admin.edit_player'", "url_for('edit_player'"),
    ("url_for('admin.edit_match'", "url_for('edit_match'"),
    ("url_for('admin.edit_news'", "url_for('edit_news'"),
    ("url_for('admin.delete_team'", "url_for('delete_team'"),
    ("url_for('admin.delete_player'", "url_for('delete_player'"),
    ("url_for('admin.delete_match'", "url_for('delete_match'"),
    ("url_for('admin.delete_news'", "url_for('delete_news'"),
    ("url_for('admin.delete_user'", "url_for('delete_user'"),
    ("url_for('admin.enter_result'", "url_for('enter_result'"),
    ("url_for('admin.approve_transfer'", "url_for('approve_transfer'"),
    ("url_for('admin.reject_transfer'", "url_for('reject_transfer'"),

    # Public blueprint replacements
    ("url_for('public.home'", "url_for('home'"),
    ("url_for('public.league_table'", "url_for('league_table'"),
    ("url_for('public.table'", "url_for('league_table'"),
    ("url_for('public.fixtures'", "url_for('fixtures'"),
    ("url_for('public.results'", "url_for('results'"),
    ("url_for('public.teams'", "url_for('teams'"),
    ("url_for('public.team_detail'", "url_for('team_detail'"),
    ("url_for('public.news'", "url_for('news'"),
    ("url_for('public.news_detail'", "url_for('news_detail'"),
    ("url_for('public.scorers'", "url_for('scorers'"),

    # Auth blueprint replacements
    ("url_for('auth.login'", "url_for('login'"),
    ("url_for('auth.logout'", "url_for('logout'"),

    # Captain blueprint replacements
    ("url_for('captain.dashboard'", "url_for('dashboard'"),
    ("url_for('captain.squad'", "url_for('squad'"),
    ("url_for('captain.transfers'", "url_for('transfers'"),
    ("url_for('captain.lineups'", "url_for('lineups'"),
    ("url_for('captain.lineup_form'", "url_for('lineup_form'"),
    ("url_for('captain.submit_lineup'", "url_for('submit_lineup'"),
    ("url_for('captain.upload_player_photo'", "url_for('upload_player_photo'"),
    ("url_for('captain.set_price'", "url_for('set_price'"),
    ("url_for('captain.request_transfer'", "url_for('request_transfer'"),
]

# Find all HTML files recursively
html_files = glob.glob('**/*.html', recursive=True)
fixed_count = 0
total_replacements = 0

for html_file in html_files:
    # Skip the fix scripts themselves
    if 'fix' in html_file or 'final' in html_file:
        continue
    
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Apply all replacements
        for old, new in REPLACEMENTS:
            content = content.replace(old, new)
        
        # Only write if changes were made
        if content != original_content:
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(content)
            
            # Count replacements
            replacements_made = sum(
                original_content.count(old) - content.count(old)
                for old, new in REPLACEMENTS
            )
            if replacements_made > 0:
                print(f"FIXED: {html_file} ({replacements_made} replacements)")
                fixed_count += 1
                total_replacements += replacements_made
    except Exception as e:
        print(f"ERROR processing {html_file}: {e}")

print(f"\n✅ FINAL SUCCESS!")
print(f"Files modified: {fixed_count}")
print(f"Total replacements: {total_replacements}")
