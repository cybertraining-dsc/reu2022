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
counties under subdirectories. The files consist of `.txt` files named after
different states/counties.

The following files have been created:
```python
States
States/CT!.txt
States/CT1.txt
States/NJ1.txt
States/NJ2.txt
States/VA1.txt
States/VA Counties
States/VA Counties/Albemarle.txt
```

For this case and other cases, use the command `glob` to search for the files.
In this case, an asterisk (*) can be used to search for any files in a given
directory. 

Shown here is an example of the `glob` command with the asterisk being used.

```python
import glob

for name in sorted(glob.glob('Years/*')):
    print(name)
```

The output shown here is a list of every single file under the directory `States`
in alphabetical order.

```
States\CT!.txt
States\CT.txt
States\NJ.txt
States\NJ1.txt
States\VA Counties
States\VA.txt
```

## Single Character Wildcard (?)

A question mark (?) can be used with the `glob` command to 