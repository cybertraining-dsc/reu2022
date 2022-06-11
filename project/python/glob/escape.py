import glob

specials = '!+('

for char in specials:
    pattern = 'tmp/*' + glob.escape(char) + '.txt'
    for name in sorted(glob.glob(pattern)):
        print(name)