import glob

print('Named explicitly:')
for name in sorted(glob.glob('updates/patches/*')):
    print('  {}'.format(name))

print('Named with wildcard:')
for name in sorted(glob.glob('updates/*/*')):
    print('  {}'.format(name))