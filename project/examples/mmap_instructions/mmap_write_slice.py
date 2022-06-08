import mmap
import shutil

# Copy the example file
shutil.copyfile('story.txt', 'story_copy.txt')

word = b'time'
reversed = word[::-1]
print('Looking for    :', word)
print('Replacing with :', reversed)

with open('story_copy.txt', 'r+') as f:
    with mmap.mmap(f.fileno(), 0) as m:
        print('Before:\n{}'.format(m.readline().rstrip()))
        m.seek(0)  # rewind

        loc = m.find(word)
        m[loc:loc + len(word)] = reversed
        m.flush()

        m.seek(0)  # rewind
        print('After :\n{}'.format(m.readline().rstrip()))

        f.seek(0)  # rewind
        print('File  :\n{}'.format(f.readline().rstrip()))