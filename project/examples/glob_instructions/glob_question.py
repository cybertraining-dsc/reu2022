import glob

for name in sorted(glob.glob('Updates/version2-?.txt')):
    print(name)
