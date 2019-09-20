#!/usr/bin/python3


def best_score(a_dictionary):

    if a_dictionary is not None and a_dictionary != {}:
        if len(a_dictionary) > 1:
            sorted(a_dictionary.items(), key=lambda item: item[1])
            return list(a_dictionary.keys())[-1]
        return list(a_dictionary.keys())[0]
    else:
        return None
