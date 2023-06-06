#!/usr/bin/python3
"""text_indentation function"""


def text_indentation(text):
    """Prints text after the sign ".", "?", and ":" """

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    sign = ['?', '.', ':']

    for c in sign:
        text = text.replace(c, c + "\n\n")
    
    listed_lines = [lines.strip(' ') for lines in text.split('\n')]
    
    newline = "\n".join(listed_lines)
    
    print(newline, end="")
