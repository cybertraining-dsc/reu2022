import glob

for name in sorted(glob.glob('tmp/a-?.txt')):
    print(name)
