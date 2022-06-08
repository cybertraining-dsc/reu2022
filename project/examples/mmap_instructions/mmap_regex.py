import mmap
import re

pattern = re.compile(rb'(\.\W+)?([^.]?im[^.]*?\.)',
                     re.DOTALL | re.IGNORECASE | re.MULTILINE)

with open('story.txt', 'r') as f:
    with mmap.mmap(f.fileno(), 0,
                   access=mmap.ACCESS_READ) as m:
        for match in pattern.findall(m):
            print(match[1].replace(b'\n', b' '))