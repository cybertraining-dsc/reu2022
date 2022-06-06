import shelve
import pprint

with shelve.open('fav_color.db', writeback=True) as s:
    print('Initial data:')
    pprint.pprint(s['votes'])

    s['votes']['green'] = 5
    print('\nModified:')
    pprint.pprint(s['votes'])

with shelve.open('fav_color.db', writeback=True) as s:
    print('\nPreserved:')
    pprint.pprint(s['votes'])