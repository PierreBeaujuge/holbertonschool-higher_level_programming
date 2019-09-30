#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):

    i = 0
    new_list = []
    for i in range(list_length):
        result = 0
        try:
            result = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            new_list.append(result)
    return new_list

#    new_list = []
#    for a, b in zip(my_list_1, my_list_2):
#        try:
#            result = a / b
#        except TypeError:
#            result = 0
#            print("wrong type")
#        except ZeroDivisionError:
#            result = 0
#            print("division by 0")
#        finally:
#            new_list.append(result)
#    if len(my_list_1) > len(my_list_2) and list_length > len(my_list_2):
#        for i in range((list_length + 1) - len(my_list_1)):
#            print("out of range")
#            new_list.append(0)
#    elif len(my_list_2) > len(my_list_1) and list_length > len(my_list_1):
#        for i in range((list_length + 1) - len(my_list_2)):
#            print("out of range")
#            new_list.append(0)
#    return new_list
