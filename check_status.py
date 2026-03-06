import re
with open('app.py', 'r') as f:
    content = f.read()

# Find references
patterns = ['public.home', 'admin.dashboard', 'captain.dashboard', 'auth.login']
for p in patterns:
    count = content.count(f"url_for('{p}'")
    if count > 0:
        print(f"Found {count}x url_for('{p}' - NEEDS FIXING")
    else:
        print(f"✓ No url_for('{p}' found")
