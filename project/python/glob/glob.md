#  glob

`glob` is a small module that searches for files by reading the
patterns of filenames.  However, `glob` doesn't work in the same way
regular expressions do as they follow standard Unix path expansion
rules.

## Glob with asterisk

The example showcases different states under a single directory and 
counties under subdirectories. The files consist of `.txt` files consisting of 
different versions of a program under a single directory.  Let us first create 
some file sin a temporary directory:

```bash
$ cd
$ mkdir tmp/subdir
$ touch tmp/a.txt
$ touch tmp/a-1.txt
$ touch tmp/b.txt
$ touch tmp/b+.txt
$ touch tmp/subdir/c.txt
```

Now let us create the following 
[file](https://github.com/cybertraining-dsc/reu2022/blob/main/project/examples/glob_instructions/glob_asterisk.py)
file in the home directory. To list all the file in the tmp directory you can 
use the asterisk '*': 

```python
import glob

for name in sorted(glob.glob('tmp/*')):
    print(name)
```

It will list the files in the directory tmp 
in alphabetical order.

```
tmp/a.txt
tmp/a-1.txt
tmp/b.txt
tmp/b+.txt
```

## Single Character Wildcard (?)

A question mark (?) can be used to search for files with the same pattern of 
names through singling out one character as a wildcard. This can be shown in
this [example](https://github.com/cybertraining-dsc/reu2022/blob/main/project/examples/glob_instructions/glob_question.py).

```python
import glob

for name in sorted(glob.glob('tmp/a-?.txt')):
    print(name)
```

This program lists the files starting with `a-`, a single character
and as prefix `.txt`

```
tmp/a-1.txt
```

## Escape Characters

`glob` can also search for files that contain a special characters through using 
the command `glob.escape(char)`. This can be shown in this [example](https://github.com/cybertraining-dsc/reu2022/blob/main/project/examples/glob_instructions/glob_escape.py).

```python
import glob

specials = '!+('

for char in specials:
    pattern = 'tmp/*' + glob.escape(char) + '.txt'
    for name in sorted(glob.glob(pattern)):
        print(name)
```

The output shown here is a every file that specifically contains the characters
`!`, `+`, or `(`. There is only file that does so which is:

```
tm/b+.txt
```

## Subdirectories

Not only `glob` can search for files recursively in directries with
the `**` query

```python
import glob


for name in sorted(glob.glob('tmp/**')):
    print(name)

```

In this example, will produce

```
tmp/subdir
tmp/a.txt
tmp/a-1.txt
tmp/b.txt
tmp/b+.txt
tmp/subdir/c.txt
```

## Links

* [Glob Documentation](https://pymotw.com/3/glob/index.html>)

