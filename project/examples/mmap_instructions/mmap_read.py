import mmap

with open('story.txt', 'r') as f:
    with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as m:
        print('First 10 bytes (Read) :', m.read(10))
        print('First 10 bytes (Slice):', m[:10])
        print('Second 10 bytes (Read) :', m.read(10))