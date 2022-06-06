import shelve

with shelve.open('fav_color.db') as s:
    s['votes'] = {
        'red': 5,
        'blue': 3,
        'yellow': 2,
    }