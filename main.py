import logic
from plant import Plant

"""
Main is the entry point of the project. It will control all the user interaction within the console
and call the appropriate logic functions to execute the user's commands.

TODO: create flow to take user input to save, update, create and delete plants
"""


def main():
    print(
        """
    ,,,                      ,,,
   {{{}}    ,,,             {{{}}    ,,,
,,, ~Y~    {{{}},,,      ,,, ~Y~    {{{}},,,
{{}}} |/,,,  ~Y~{{}}}    {{}}} |/,,,  ~Y~{{}}}
~Y~ \|{{}}}/\|/ ~Y~  ,,, ~Y~ \|{{}}}/\|/ ~Y~  ,,,
\|/ \|/~Y~  \|,,,|/ {{}}}\|/ \|/~Y~  \|,,,|/ {{}}}
\|/ \|/\|/  \{{{}}/  ~Y~ \|/ \|/\|/  \{{{}}/  ~Y~
\|/\|/\|/ \|~Y~//  \|/ \|/\|/\|/ \|~Y~//  \|/
\|//\|/\|/,\|/|/|// \|/ \|//\|/\|/,\|/|/|// \|/
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        PLANT PROJECT (IN DEVELOPMENT)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    """
    )
    __print_plant_header()
    logic.print_all_plants()
    __print_options()

    while True:
        command = input()
        __execute_response(command)


def __execute_response(command):
    if command == "1":
        __print_plant_header()
        logic.print_all_plants()
    elif command == "2":
        print("add a plant")
    elif command == "3":
        print("update plant info")
    elif command == "4":
        print("delete plant")
    elif command == "exit":
        quit()
    else:
        print(f"{command} is not a valid commmand")
        __print_options()


def __print_options():
    print(
        """   
        
          Enter Option:
          
          1 - display current plant info
          2 - add new plant
          3 - update plant info
          4 - delete plant
          
        """
    )


def __print_plant_header():
    print("{:<20} {:<20} {:<20}".format("Name", "Last Watered", "Water per Week") + "\n")


main()
