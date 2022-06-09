import glob
for name in sorted(glob.glob('updates/*[0-9].*')):
    print(name)