import mmap

with open('story.txt', 'r') as f:
    with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as m:
        print('Char. 1-10 (Read) :', m.read(10))
        print('Char. 1-10 (Slice):', m[:10])
        print('Char. 11-20 (Read) :', m.read(10))