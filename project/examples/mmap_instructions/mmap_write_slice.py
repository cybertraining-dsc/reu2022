import mmap
import shutil

# Copy the example file
shutil.copyfile('story.txt', 'story_copy.txt')

word = b'barnacle'

with open('story_copy.txt', 'r+') as f:
    with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE) as m:

# Memory-map file before change

        print('Memory Before:\n{}'.format(m.readline().rstrip()))
        m.seek(0)  # rewind

        loc = m.find(word)
        m[loc:loc + len(word)] = b'seahorse'
        m.flush()

# Memory-map file after change

        m.seek(0)  # rewind
        print('Memory After:\n{}'.format(m.readline().rstrip()))

# Actual file after change

        f.seek(0)  # rewind
        print('File After:\n{}'.format(f.readline().rstrip()))

