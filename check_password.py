import sqlite3

conn = sqlite3.connect('football_league_rebranded/instance/football.db')
c = conn.cursor()
c.execute('SELECT username, password_hash FROM users WHERE username = ?', ('admin',))
row = c.fetchone()
if row:
    print(f"Found admin user:")
    print(f"  Username: {row[0]}")
    print(f"  Password hash: {row[1][:50]}...")
else:
    print("Admin user not found!")
conn.close()
