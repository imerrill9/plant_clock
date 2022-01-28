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
    logic.print_plant_header()
    logic.print_all_plants()


main()
