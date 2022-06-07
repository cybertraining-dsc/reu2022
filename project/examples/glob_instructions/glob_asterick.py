import glob

for name in sorted(glob.glob('Updates/*')):
    print(name)
