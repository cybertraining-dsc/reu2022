import glob

print('Named explicitly:')
for name in sorted(glob.glob('Updates/Patches/*')):
    print('  {}'.format(name))

print('Named with wildcard:')
for name in sorted(glob.glob('Updates/*/*')):
    print('  {}'.format(name))