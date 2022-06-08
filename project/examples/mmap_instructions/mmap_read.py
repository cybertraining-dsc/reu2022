import mmap

with open('story.txt', 'r') as f:
    with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as m:

# Reads the first ten characters
        print('Char. 1-10 (Read) :', m.read(10))

# Reads a slice of characters
        print('Char. 1-10 (Slice):', m[5:14])

# Reads the next ten characters
        print('Char. 11-20 (Read) :', m.read(10))