# Summary of `mmap`

`mmap` standards for memory-map files. Memory-mapping a file involves accessing
files directly without the use of traditional I/O functions.

## Import Statement

These should be the very first lines a user must write before proceeding:

```python
import mmap
```

## Reading

The example shown here is a short, simple story that is contained in a `.txt`
file. The file can be accessed [here](https://github.com/cybertraining-dsc/reu2022/blob/main/project/examples/mmap_instructions/story.txt).

```
Once upon a time there was an ugly barnacle. He was so ugly that everyone died. The end!
```

First, the file can be opened traditionally using the `open` command with the parameter `'r'` for 
reading. In this example, this command is assigned to `f`. 
The memory-map file can be created using the command `mmap.mmap()`. Within the parentheses `()`,
various arguments should be made. The first argument should be `f.fileno()`


```python
import mmap

with open('story.txt', 'r') as f:
    with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as m:

# Reads the first ten characters
        print('Char. 1-10 (Read) :', m.read(10))

# Reads a slice of characters
        print('Char. 1-10 (Slice):', m[5:14])

# Reads the next ten characters
        print('Char. 11-20 (Read) :', m.read(10))
```

## Writing

## Sources

* <https://pymotw.com/3/mmap/index.html>