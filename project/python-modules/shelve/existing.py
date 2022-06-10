import shelve

with shelve.open('fav_color.db') as s:
    existing = s['votes']

print(existing)