import glob

specials = '!+('

for char in specials:
    pattern = 'Updates/*' + glob.escape(char) + '.txt'
    for name in sorted(glob.glob(pattern)):
        print(name)