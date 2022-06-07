import glob
for name in sorted(glob.glob('Updates/*[0-9].*')):
    print(name)