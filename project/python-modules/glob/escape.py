import glob

specials = '!+('

for char in specials:
    pattern = 'updates/*' + glob.escape(char) + '.txt'
    for name in sorted(glob.glob(pattern)):
        print(name)