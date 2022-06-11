import glob

for name in sorted(glob.glob('tmp/*')):
    print(name)
