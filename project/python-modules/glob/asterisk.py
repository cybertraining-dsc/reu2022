import glob

for name in sorted(glob.glob('updates/*')):
    print(name)
