#!/usr/bin/env python3
"""
Fix all blueprint-style endpoint references in the entire project.
Handles both Python code and template files.
"""

import os
import re

# All replacements needed
REPLACEMENTS = [
    # public.* endpoints
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
    
    # admin.* endpoints
    ("url_for('admin.dashboard'", "url_for('admin_dashboard'"),
    ("url_for('admin.teams'", "url_for('admin_teams'"),
    ("url_for('admin.players'", "url_for('admin_players'"),
    ("url_for('admin.matches'", "url_for('admin_matches'"),
    ("url_for('admin.enter_result'", "url_for('enter_result'"),
    ("url_for('admin.add_match'", "url_for('add_match'"),
    ("url_for('admin.edit_match'", "url_for('edit_match'"),
    ("url_for('admin.delete_match'", "url_for('delete_match'"),
    ("url_for('admin.add_team'", "url_for('add_team'"),
    ("url_for('admin.edit_team'", "url_for('edit_team'"),
    ("url_for('admin.delete_team'", "url_for('delete_team'"),
    ("url_for('admin.add_player'", "url_for('add_player'"),
    ("url_for('admin.edit_player'", "url_for('edit_player'"),
    ("url_for('admin.delete_player'", "url_for('delete_player'"),
    ("url_for('admin.transfers'", "url_for('admin_transfers'"),
    ("url_for('admin.approve_transfer'", "url_for('approve_transfer'"),
    ("url_for('admin.reject_transfer'", "url_for('reject_transfer'"),
    ("url_for('admin.news'", "url_for('admin_news'"),
    ("url_for('admin.add_news'", "url_for('add_news'"),
    ("url_for('admin.edit_news'", "url_for('edit_news'"),
    ("url_for('admin.delete_news'", "url_for('delete_news'"),
    ("url_for('admin.users'", "url_for('admin_users'"),
    ("url_for('admin.add_user'", "url_for('add_user'"),
    ("url_for('admin.delete_user'", "url_for('delete_user'"),
    ("url_for('admin.add_money'", "url_for('add_money'"),
    
    # captain.* endpoints
    ("url_for('captain.dashboard'", "url_for('dashboard'"),
    ("url_for('captain.squad'", "url_for('squad'"),
    ("url_for('captain.transfers'", "url_for('captain_transfers'"),
    ("url_for('captain.lineups'", "url_for('lineups'"),
    
    # auth.* endpoints
    ("url_for('auth.login'", "url_for('login'"),
    ("url_for('auth.logout'", "url_for('logout'"),
]

def fix_file(filepath):
    """Fix all blueprint-style references in a file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        for old, new in REPLACEMENTS:
            content = content.replace(old, new)
        
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
    
    return False

def process_directory(root_dir, extensions):
    """Recursively process files with given extensions"""
    fixed_count = 0
    
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Skip __pycache__ and .git
        dirnames[:] = [d for d in dirnames if d not in ['__pycache__', '.git', '.venv', 'node_modules']]
        
        for filename in filenames:
            if any(filename.endswith(ext) for ext in extensions):
                filepath = os.path.join(dirpath, filename)
                if fix_file(filepath):
                    fixed_count += 1
                    print(f"✓ Fixed: {filepath}")
    
    return fixed_count

# Main
if __name__ == '__main__':
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    print("=" * 60)
    print("Fixing blueprint-style endpoint references")
    print("=" * 60)
    
    # Fix Python files
    print("\n📄 Python files (.py)...")
    python_count = process_directory(base_dir, ['.py'])
    
    # Fix template files
    print("\n🎨 Template files (.html)...")
    template_count = process_directory(base_dir, ['.html'])
    
    total = python_count + template_count
    print("\n" + "=" * 60)
    if total > 0:
        print(f"✅ Fixed {total} files total")
    else:
        print("ℹ️  No files needed fixing")
    print("=" * 60)
