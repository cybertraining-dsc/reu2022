import dbm
import shelve

with shelve.open('fav_color.db', flag='r') as s:
    print('Existing:', s['votes'])
    try:
        s['votes'] = 'green'
    except dbm.error as err:
        print('ERROR: {}'.format(err))
