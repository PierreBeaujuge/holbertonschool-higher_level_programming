#!/usr/bin/python3


def best_score(a_dictionary):

    if a_dictionary is not None and a_dictionary != {}:
        sorted_dict = sorted(a_dictionary.items(), key=lambda item: item[1])
        return (sorted_dict[-1])[0]
    else:
        return None
