#!/usr/bin/python3
"""
100-append_after module
"""


def append_after(filename="", search_string="", new_string=""):
    """
    function that inserts a line of text to a file,
    after each line containing a specific string
    """
    with open(filename, 'r') as f:
        a_dict = f.readlines()
        for i in range(len(a_dict)):
            #            b_dict = a_dict[i].split(' ')
            #            print(b_dict)
            #            for word in b_dict:
            if search_string in a_dict[i]:
                a_dict.insert(i + 1, new_string)
                i += 1
                #        print(a_dict)
    with open(filename, 'w') as wf:
        for i in range(len(a_dict)):
            wf.write(a_dict[i])
