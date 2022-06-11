import glob

print('Named explicitly:')
for name in sorted(glob.glob('TMP/**')):
    print(name)

