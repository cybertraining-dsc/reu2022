import glob

for name in sorted(glob.glob('updates/version2-?.txt')):
    print(name)
