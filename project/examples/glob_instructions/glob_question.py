import glob

for name in sorted(glob.glob('Years/NJ?.txt')):
    print(name)
