import glob
for name in sorted(glob.glob('tmp/*[0-9].*')):
    print(name)