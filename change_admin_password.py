#!/usr/bin/env python3
"""
Script to change admin password to 1234
"""

import sqlite3
from werkzeug.security import generate_password_hash
import os

db_path = 'football_league_rebranded/instance/football.db'

if not os.path.exists(db_path):
    print(f"Error: Database not found at {db_path}")
    exit(1)

conn = sqlite3.connect(db_path)
c = conn.cursor()

# Generate the new password hash
new_password_hash = generate_password_hash('1234')

# Update the admin user's password
c.execute(
    "UPDATE users SET password_hash = ? WHERE username = 'admin'",
    (new_password_hash,)
)

conn.commit()
rows_affected = c.rowcount

if rows_affected > 0:
    print(f"✓ Admin password changed successfully!")
    print(f"  Username: admin")
    print(f"  New password: 1234")
else:
    print("Error: Admin user not found in database")

conn.close()
