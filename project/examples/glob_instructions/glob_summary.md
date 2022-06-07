# Glob Summary
 
Glob is a small module that searches for files by reading the patterns of filenames.
However, Glob doesn't work in the same way regular expressions do as they follow
standard Unix path expansion rules.

## Import Statement

This should be the very first line a user must write before proceeding:

```python
import glob
```

## Wildcard (*)

The example shown here showcases different states under a single directory and 
counties under subdirectories. The files consist of `.txt` files consisting of 
different versions of a program under a single directory.

The following files have been created:
```python
Updates
Updates/Patches
Updates/Patches/patch3.txt
Updates/version2+.txt
Updates/version2-1.txt
Updates/version2-2.txt
Updates/version2-a.txt
Updates/version2-b.txt
```

For this case and other cases, use the command `glob` to search for the files.
In this case, an asterisk (*) can be used to search for any files in a given
directory. 

Shown here is an [example](https://github.com/cybertraining-dsc/reu2022/blob/main/project/examples/glob_instructions/glob_asterisk.py)
of the `glob` command with the asterisk `*` being used.

```python
import glob

for name in sorted(glob.glob('Updates/*')):
    print(name)
```

The output shown here is a list of every single file under the directory `States`
in alphabetical order.

```
Updates\Patches
Updates\version2+.txt
Updates\version2-1.txt
Updates\version2-2.txt
Updates\version2-a.txt
Updates\version2-b.txt
```

## Single Character Wildcard (?)

A question mark (?) can be used to search for files with the same pattern of 
names through singling out one character as a wildcard. This can be shown in
this [example](https://github.com/cybertraining-dsc/reu2022/blob/main/project/examples/glob_instructions/glob_question.py)

```python
import glob

for name in sorted(glob.glob('Updates/version2-?.txt')):
    print(name)
```

The output shown here is a list of every single file that consists of the series of
characters `version2-`. See here that this list doesn't include `Updates\version2+.txt`
as it doesn't consist the `-` in `version2-`.

```
Updates\version2-1.txt
Updates\version2-2.txt
Updates\version2-a.txt
Updates\version2-b.txt
```

## Escape Characters

Glob can also search for files that contain a specific character through using 
the command `glob.escape(char)`. This can be shown in this [example]
