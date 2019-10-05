#!/usr/bin/python3
"""
Module that handles
printing
of a text
"""


def text_indentation(text):
    """
    Function that prints a text with 2 new lines after ., ? and :
    """
    new_text = ""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        if text[i] is '.' or text[i] is '?' or text[i] is ':':
            new_text += text[i]
            new_text += '\n\n'
            if i < len(text) - 1 and (text[i + 1] == ' ' or
                                      text[i + 1] == '\t'):
                i += 1
                while i < len(text) - 1 and (text[i + 1] == ' ' or
                                             text[i + 1] == '\t'):
                    i += 1
        else:
            new_text += text[i]
        i += 1
    print(new_text, end='')
