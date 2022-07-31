# Mmap

`mmap` standards for memory-map files. Memory-mapping a file involves
accessing files directly without the use of traditional I/O functions.

## Reading

The example shown here is a short, simple story that is contained in a
`.txt` file. The file can be accessed
[here](https://github.com/cybertraining-dsc/reu2022/blob/main/project/examples/mmap_instructions/example.txt)
as `example.txt`.

```
Let's play with the dog, it's really nice out today!
```

First, the actual file should be opened using the `open` command with
the parameter `'r'` for reading and is indicated with the header `f`.

After that, memory-map file can be created using the command `mmap.mmap()` 
and can be indicated with the header `m`. Within the parentheses `()`, 
various arguments should be made.

The first argument should be `f.fileno()`, a file descriptor that opens and 
closes the `mmap` file.

The second argument is the size in bytes, in the form of a float, of
the portion of the file to map. If it's `0`, like in this example, the
entire file is mapped.

The third argument, which is optional, is the accessibility
settings. In this example, it's set to read-only through
`access=mmap.ACCESS_READ`.

The code in this example will read various parts of `story.txt` both
progressively and through slices.

```python
import mmap

with open('example.txt', 'r') as f:
    with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as m:
        # Reads the first ten characters
        print('Char. 1-10 (Read) :', m.read(10))

        # Reads a slice of characters
        print('Char. 1-10 (Slice):', m[5:14])

        # Reads the next ten characters
        print('Char. 11-20 (Read) :', m.read(10))
```

The following output is produced:

```
Char. 1-10 (Read) : b"Let's play"
Char. 1-10 (Slice): b' play wit'
Char. 11-20 (Read) : b' with the '
```

## Writing

In order to modify files, do the same procedure as reading files by
opening the actual file with the `open` command; however, this time,
use the parameter `r+` instead of `r`.

Then, create the `mmap` file with `mmap.mmap` with the same required
arguments. The optional argument set to the default access mode of
`access=mmap.ACCESS_WRITE` in this case.

After those commands, edits can then be made to the `mmap` file as shown in the 
following [example](https://github.com/cybertraining-dsc/reu2022/blob/main/project/examples/mmap_instructions/mmap_write_slice.py).

```python
import mmap
import shutil

# Copy the example file
shutil.copyfile('example.txt', 'example_copy.txt')

word = b'dog'

with open('example_copy.txt', 'r+') as f:
    with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE) as m:

        # Memory-map file before change

        print('Memory Before:\n{}'.format(m.readline().rstrip()))
        m.seek(0)  # rewind

        loc = m.find(word)
        m[loc:loc + len(word)] = b'cat'
        m.flush()

        # Memory-map file after change

        m.seek(0)  # rewind
        print('Memory After:\n{}'.format(m.readline().rstrip()))

        # Actual file after change

        f.seek(0)  # rewind
        print('File After:\n{}'.format(f.readline().rstrip()))
```

The following output shows that this access mode allows the modification of the
actual file.

```
Memory Before:
b"Let's play with the dog, it's really nice out today!"
Memory After:
b"Let's play with the cat, it's really nice out today!"
File After:
Let's play with the cat, it's really nice out today!
```

This can be changed by setting the access mode to `access=mmap.ACCESS_COPY` as 
shown in this [example](https://github.com/cybertraining-dsc/reu2022/blob/main/project/examples/mmap_instructions/mmap_write_copy.py).

```python
import mmap
import shutil

# Copy the example file
shutil.copyfile('example.txt', 'example_copy.txt')

word = b'dog'

# Changing access settings

with open('example_copy.txt', 'r+') as f:
    with mmap.mmap(f.fileno(), 0,
                   access=mmap.ACCESS_COPY) as m:

        # Memory-map file before change

        print('Memory Before:\n{}'.format(m.readline().rstrip()))

        # Actual file before change

        print('File Before:\n{}'.format(f.readline().rstrip()))

        m.seek(0)  # rewind
        loc = m.find(word)
        m[loc:loc + len(word)] = b'cat'

        # Memory-map file after change

        m.seek(0)  # rewind
        print('Memory After:\n{}'.format(m.readline().rstrip()))

        # Actual file after change

        f.seek(0)
        print('File After:\n{}'.format(f.readline().rstrip()))
```

The following output shows that only the `mmap` file and not the
actual file was modified in the end.

```
Memory Before:
b"Let's play with the dog, it's really nice out today!"
File Before:
Let's play with the dog, it's really nice out today!
Memory After:
b"Let's play with the cat, it's really nice out today!"
File After:
Let's play with the dog, it's really nice out today!
```

## Links

* [mmap documentation](https://pymotw.com/3/mmap/index.html>)[@www-mmap-memory]