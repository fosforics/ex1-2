#!/usr/bin/env python3

import sys

def hello(name: str) -> str:
    """
    given the input in the variable called name, return a string that says hello
    to whatever name is given to this function
    """
    # the word 'pass' below does nothing, but acts as a placeholder here. Remove it and add your own code
    # so that you do what the docstring above indicates.
    pass


# You can mess with the lines down below if you want to, but it isn't necessary to get this code working and it might
# screw things up.
if __name__ == '__main__':
    print(hello(sys.argv[1]))
