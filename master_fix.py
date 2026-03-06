#!/usr/bin/env python3
"""
Master endpoint fix - replaces all remaining blueprint-style URLs throughout the project
"""
import os
import glob

# Change to project root
os.chdir(r'c:\Users\FML\Desktop\football_league_rebranded\EIALEG')

# Define exact replacements
REPLACEMENTS = {
    "url_for('admin.teams')": "url_for('admin_teams')",
    "url_for('admin.players')": "url_for('admin_players')",
    "url_for('admin.matches')": "url_for('admin_matches')",
    "url_for('admin.dashboard')": "url_for('admin_dashboard')",
    "url_for('admin.transfers')": "url_for('admin_transfers')",
    "url_for('admin.news')": "url_for('admin_news')",
    "url_for('admin.users')": "url_for('admin_users')",
    "url_for('admin.add_team')": "url_for('add_team')",
    "url_for('admin.add_player')": "url_for('add_player')",
    "url_for('admin.add_match')": "url_for('add_match')",
    "url_for('admin.add_news')": "url_for('add_news')",
    "url_for('admin.add_user')": "url_for('add_user')",
    "url_for('admin.add_money')": "url_for('admin_add_money')",
    "url_for('admin.enter_result')": "url_for('admin_enter_result')",
    "url_for('admin.edit_team')": "url_for('admin_edit_team')",
    "url_for('admin.edit_player')": "url_for('admin_edit_player')",
    "url_for('admin.edit_match')": "url_for('admin_edit_match')",
    "url_for('admin.edit_news')": "url_for('admin_edit_news')",
    "url_for('admin.delete_team')": "url_for('admin_delete_team')",
    "url_for('admin.delete_player')": "url_for('admin_delete_player')",
    "url_for('admin.delete_match')": "url_for('admin_delete_match')",
    "url_for('admin.delete_news')": "url_for('admin_delete_news')",
    "url_for('admin.delete_user')": "url_for('admin_delete_user')",
    "url_for('admin.approve_transfer')": "url_for('admin_approve_transfer')",
    "url_for('admin.reject_transfer')": "url_for('admin_reject_transfer')",
    "url_for('public.home')": "url_for('home')",
    "url_for('public.league_table')": "url_for('league_table')",
    "url_for('public.fixtures')": "url_for('fixtures')",
    "url_for('public.results')": "url_for('results')",
    "url_for('public.teams')": "url_for('public_teams')",
    "url_for('public.team_detail')": "url_for('team_detail')",
    "url_for('public.news')": "url_for('news')",
    "url_for('auth.login')": "url_for('login')",
    "url_for('auth.logout')": "url_for('logout')",
    "url_for('captain.dashboard')": "url_for('captain_dashboard')",
    "url_for('captain.squad')": "url_for('captain_squad')",
    "url_for('captain.transfers')": "url_for('captain_transfers')",
    "url_for('captain.lineups')": "url_for('captain_lineups')",
    "url_for('captain.submit_lineup')": "url_for('captain_submit_lineup')",
    "url_for('captain.upload_player_photo')": "url_for('captain_upload_player_photo')",
    "url_for('captain.set_price')": "url_for('captain_set_price')",
    "url_for('captain.request_transfer')": "url_for('captain_request_transfer')",
}

# Find and fix all HTML files
count_files = 0
count_replacements = 0

for html_file in glob.glob('**/*.html', recursive=True):
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        
        for old, new in REPLACEMENTS.items():
            while old in content:
                content = content.replace(old, new,1)
                count_replacements += 1
        
        if content != original:
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(content)
            count_files += 1
            print(f'FIXED: {html_file}')
    except Exception as e:
        pass  # Skip errors

print(f'\n\n✅ SUCCESS!')
print(f'Files modified: {count_files}')
print(f'Total replacements: {count_replacements}')
