#!/usr/bin/env python3
import os
os.chdir(r'c:\Users\FML\Desktop\football_league_rebranded\EIALEG')

# Read app.py
with open('app.py', 'r', encoding='utf-8') as f:
    content = f.read()

# All replacements - exactly as they appear in the file
replacements = {
    "url_for(\\'admin.dashboard\\')": "url_for(\\'admin_dashboard\\')",
    "url_for(\\'admin.teams\\')": "url_for(\\'admin_teams\\')",
    "url_for(\\'admin.players\\')": "url_for(\\'admin_players\\')",
    "url_for(\\'admin.matches\\')": "url_for(\\'admin_matches\\')",
    "url_for(\\'admin.transfers\\')": "url_for(\\'admin_transfers\\')",
    "url_for(\\'admin.news\\')": "url_for(\\'admin_news\\')",
    "url_for(\\'admin.users\\')": "url_for(\\'admin_users\\')",
    "url_for(\\'admin.add_news\\')": "url_for(\\'add_news\\')",
    "url_for(\\'admin.add_user\\')": "url_for(\\'add_user\\')",
    "url_for(\\'admin.add_match\\')": "url_for(\\'add_match\\')",
    "url_for(\\'admin.add_team\\')": "url_for(\\'add_team\\')",
    "url_for(\\'admin.add_player\\')": "url_for(\\'add_player\\')",
    "url_for(\\'admin.enter_result\\')": "url_for(\\'admin_enter_result\\')",
    "url_for(\\'admin.edit_match\\')": "url_for(\\'admin_edit_match\\')",
    "url_for(\\'admin.delete_match\\')": "url_for(\\'admin_delete_match\\')",
    "url_for(\\'admin.edit_news\\')": "url_for(\\'admin_edit_news\\')",
    "url_for(\\'admin.delete_news\\')": "url_for(\\'admin_delete_news\\')",
    "url_for(\\'admin.edit_team\\')": "url_for(\\'admin_edit_team\\')",
    "url_for(\\'admin.delete_team\\')": "url_for(\\'admin_delete_team\\')",
    "url_for(\\'admin.edit_player\\')": "url_for(\\'admin_edit_player\\')",
    "url_for(\\'admin.delete_player\\')": "url_for(\\'admin_delete_player\\')",
    "url_for(\\'admin.approve_transfer\\')": "url_for(\\'admin_approve_transfer\\')",
    "url_for(\\'admin.reject_transfer\\')": "url_for(\\'admin_reject_transfer\\')",
    "url_for(\\'admin.add_money\\')": "url_for(\\'admin_add_money\\')",
    "url_for(\\'public.home\\')": "url_for(\\'home\\')",
    "url_for(\\'public.league_table\\')": "url_for(\\'league_table\\')",
    "url_for(\\'public.fixtures\\')": "url_for(\\'fixtures\\')",
    "url_for(\\'public.results\\')": "url_for(\\'results\\')",
    "url_for(\\'public.teams\\')": "url_for(\\'public_teams\\')",
    "url_for(\\'public.team_detail\\')": "url_for(\\'team_detail\\')",
    "url_for(\\'public.news\\')": "url_for(\\'news\\')",
    "url_for(\\'public.scorers\\')": "url_for(\\'scorers\\')",
    "url_for(\\'auth.login\\')": "url_for(\\'login\\')",
    "url_for(\\'auth.logout\\')": "url_for(\\'logout\\')",
    "url_for(\\'captain.dashboard\\')": "url_for(\\'captain_dashboard\\')",
    "url_for(\\'captain.squad\\')": "url_for(\\'captain_squad\\')",
    "url_for(\\'captain.transfers\\')": "url_for(\\'captain_transfers\\')",
    "url_for(\\'captain.lineups\\')": "url_for(\\'captain_lineups\\')",
    "url_for(\\'captain.submit_lineup\\')": "url_for(\\'captain_submit_lineup\\')",
    "url_for(\\'captain.upload_player_photo\\')": "url_for(\\'captain_upload_player_photo\\')",
    "url_for(\\'captain.set_price\\')": "url_for(\\'captain_set_price\\')",
    "url_for(\\'captain.request_transfer\\')": "url_for(\\'captain_request_transfer\\')",
}

count = 0
for old, new in replacements.items():
    if old in content:
        count_old = content.count(old)
        content = content.replace(old, new)
        print(f"✓ Replaced {count_old:3d}x: {old[:50]}")
        count += count_old

# Write back
with open('app.py', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"\n✅ Total replacements made: {count}")
print("Fix complete! All blueprint-style endpoints have been converted.")
