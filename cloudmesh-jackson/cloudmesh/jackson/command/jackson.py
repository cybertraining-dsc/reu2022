from cloudmesh.common.console import Console
from cloudmesh.common.debug import VERBOSE
from cloudmesh.common.parameter import Parameter
from cloudmesh.common.variables import Variables
from cloudmesh.shell.command import PluginCommand
from cloudmesh.shell.command import command
from cloudmesh.shell.command import map_parameters


class JacksonCommand(PluginCommand):

    # noinspection PyUnusedLocal
    @command
    def do_jackson(self, args, arguments):
        """
        ::

          Usage:
                jackson --file=FILE
                jackson list
                jackson photo
                jackson animate [--percentage=PERCENTAGE]
                jackson [--parameter=PARAMETER] [--experiment=EXPERIMENT] [COMMAND...]

          This command does some useful things.

          Arguments:
              FILE   a file name
              PARAMETER  a parameterized parameter of the form "a[0-3],a5"
              PERCENTAGE  end position of the animation in relation to terminal width [default: 50]


          Options:
              -f      specify the file
              --percentage=PERCENTAGE  blahs blah [default: 50]

          Description:

            > cms jackson --parameter="a[1-2,5],a10"
            >    example on how to use Parameter.expand. See source code at
            >      https://github.com/cloudmesh/cloudmesh-jackson/blob/main/cloudmesh/jackson/command/jackson.py
            >    prints the expanded parameter as a list
            >    ['a1', 'a2', 'a3', 'a4', 'a5', 'a10']

            > jackson exp --experiment=a=b,c=d
            > example on how to use Parameter.arguments_to_dict. See source code at
            >      https://github.com/cloudmesh/cloudmesh-jackson/blob/main/cloudmesh/jackson/command/jackson.py
            > prints the parameter as dict
            >   {'a': 'b', 'c': 'd'}

        """

        # arguments.FILE = arguments['--file'] or None

        # switch debug on

        variables = Variables()
        variables["debug"] = True

        map_parameters(arguments, "file", "parameter", "experiment", "percentage")
        if (arguments.percentage):
            arguments.percentage = int(arguments.percentage)


        arguments = Parameter.parse(arguments,
                                    parameter='expand',
                                    experiment='dict',
                                    COMMAND='str')

        VERBOSE(arguments)

        #
        # It is important to keep the programming here to a minimum and any substantial programming ought
        # to be conducted in a separate class outside the command parameter manipulation. If between the
        # elif statement you have more than 10 lines, you may consider putting it in a class that you import
        # here and have proper methods in that class to handle the functionality. See the Manager class for
        # an example.
        #
        if arguments.photo:
            from cloudmesh.jackson.Jackson import Jackson
            Console.warning("No photo for you")
            jackson = Jackson()
            print(jackson.photo())
            return ""
        elif arguments.animate:
            from cloudmesh.jackson.Jackson import Jackson
            Console.warning("No photo for you")
            jackson = Jackson()
            if 0 <= arguments.percentage <= 100:
                jackson.animate(percentage=arguments.percentage)
            else:
                Console.error("Invalid percentage. Must be 0 to 100.")
            return ""
        elif arguments.file:
            print("option a")

        elif arguments.list:
            print("option b")

        return ""
