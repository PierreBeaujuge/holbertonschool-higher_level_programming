#!/usr/bin/python3
"""
Singly linked list
"""


class Node:
    """define variables and methods"""

    def __init__(self, data, next_node=None):
        """initialize attibute"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """getter for data"""
        return self.__data

    @data.setter
    def data(self, value):
        """setter for data"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """getter for next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """setter for next_node"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:
    """define variables and methods """

    def __init__(self):
        """initialize attibute"""
        self.__head = None

    def sorted_insert(self, value):
        """function that inserts a new_node"""
