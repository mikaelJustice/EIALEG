#!/usr/bin/env python3
import os
import glob

os.chdir(r'c:\Users\FML\Desktop\football_league_rebranded\EIALEG\football_league_rebranded\templates')

replacements = {
    "url_for('admin.teams')": "url_for('admin_teams')",
    "url_for('admin.players')": "url_for('admin_players')",
    "url_for('admin.matches')": "url_for('admin_matches')",
    "url_for('admin.transfers')": "url_for('admin_transfers')",
    "url_for('admin.news')": "url_for('admin_news')",
    "url_for('admin.users')": "url_for('admin_users')",
    "url_for('admin.add_news')": "url_for('add_news')",
    "url_for('admin.add_user')": "url_for('add_user')",
    "url_for('admin.add_match')": "url_for('add_match')",
    "url_for('admin.add_team')": "url_for('add_team')",
    "url_for('admin.add_player')": "url_for('add_player')",
    "url_for('admin.enter_result')": "url_for('admin_enter_result')",
    "url_for('admin.edit_match')": "url_for('admin_edit_match')",
    "url_for('admin.delete_match')": "url_for('admin_delete_match')",
    "url_for('admin.edit_news')": "url_for('admin_edit_news')",
    "url_for('admin.delete_news')": "url_for('admin_delete_news')",
    "url_for('admin.edit_team')": "url_for('admin_edit_team')",
    "url_for('admin.delete_team')": "url_for('admin_delete_team')",
    "url_for('admin.edit_player')": "url_for('admin_edit_player')",
    "url_for('admin.delete_player')": "url_for('admin_delete_player')",
    "url_for('admin.approve_transfer')": "url_for('admin_approve_transfer')",
    "url_for('admin.reject_transfer')": "url_for('admin_reject_transfer')",
    "url_for('admin.add_money')": "url_for('admin_add_money')",
    "url_for('public.home')": "url_for('home')",
    "url_for('public.teams')": "url_for('public_teams')",
    "url_for('public.team_detail')": "url_for('team_detail')",
    "url_for('auth.logout')": "url_for('logout')",
}

# Process all HTML files
for fpath in glob.glob('**/*.html', recursive=True):
    try:
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        orig = content
        for old, new in replacements.items():
            content = content.replace(old, new)
        
        if content != orig:
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f'✓ {fpath}')
    except Exception as e:
        print(f'✗ {fpath}: {e}')

print('\n✅ All template files processed!')
