import textwrap
import os
import time
from cloudmesh.common.Shell import Shell
from cloudmesh.common.systeminfo import os_is_windows


class Jackson:

    def __init__(self, text=None):
        if (text is None):
            self.text = self.photo()
        else:
            self.text = text

    def photo(self):

        art = textwrap.dedent("""
                Earth
                _____
            ,-:` \;',`'-, 
          .'-;_,;  ':-;_,'.
         /;   '/    ,  _`.-\\
        | '`. (`     /` ` \`|
        |:.  `\`-.   \_   / |
        |     (   `,  .`\ ;'|
         \     | .'     `-'/
          `.   ;/        .'
        jgs `'-._____.
        """)
        return art

    def animate(self, percentage=50):


        dividor = 100 / percentage
        print(f"here is dividor {dividor}")
        if os_is_windows:
            rows,columns = Shell.run("stty size").strip().split()
            columns = int(columns)
        else:
            size = os.get_terminal_size()
            columns = size.columns
        terminal_width = int(columns / dividor)
        columns = terminal_width - int(self.width()/dividor)
        for column in range(0, columns):
            os.system("clear")
            earth = textwrap.indent(self.text, column * " ")
            print(earth)
            time.sleep(0.05)

    def width(self):
        max = 0
        for line in self.text.splitlines():
            if (len(line) > max):
                max = len(line)

        return max
