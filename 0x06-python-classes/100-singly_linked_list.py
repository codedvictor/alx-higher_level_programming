#!/usr/bin/python3
"""class node defines a node of a singly linked list"""

class Node:
    def __init__(self, data, next_node=None):
        if type(data) is not int:
            raise TypeError("data must be an integer")
        if next_node is not None and type(next_node) is not Node:
            raise TypeError("next_node must be a Node object")
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value
    
    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and type(value) is not Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:
    """Singly linked list head and function creation"""


    def __init__(self):
        """initialize the head"""
        self.__head = None


    def __repr__(self):
        """return string of a data"""
        strreturn = ""
        if self.__head is None:
            pass
        else:
            val = self.__head
            while val is not None:
                strreturn += str(val.data) + '\n'
                val = val.next_node
        return strreturn[:-1]

    def sorted_insert(self, value):
        """insert and sort list"""
        if type(value) is not int:
            raise TypeError("data must be an integer")
        if self.__head is None:
            self.__head = Node(value)
        elif value < self.__head.data:
            self.__head = Node(value, self.__head)
        else:
            newpr = self.__head
            while newpr.next_node is not None and newpr.next_node.data < value:
                newpr = newpr.next_node
            if newpr.next_node is None:
                newpr.next_node = Node(value)
            else:
                newpr.next_node = Node(value, newpr.next_node)
