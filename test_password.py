import sqlite3
from werkzeug.security import check_password_hash

conn = sqlite3.connect('football_league_rebranded/instance/football.db')
c = conn.cursor()
c.execute('SELECT username, password_hash FROM users WHERE username = ?', ('admin',))
row = c.fetchone()

if row:
    username, password_hash = row
    test_password = '1234'
    is_correct = check_password_hash(password_hash, test_password)
    print(f"Username: {username}")
    print(f"Testing password '1234': {is_correct}")
else:
    print("Admin user not found!")
    
conn.close()
