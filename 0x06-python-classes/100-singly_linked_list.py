#!/usr/bin/python3
"""class node defines a node of a singly linked list"""

class Node:
    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__value =  value
        data = value
        if type(data) is not int:
            raise TypeError("data must be an integer")
    
    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        self.__value = value
        next_node = value
        if next_node is not None or type(next_node) is not Node:
            raise TypeError("next_node must be a Node object")

class SinglyLinkedList:
    def __init__(self):
        self.__head = head
        for i in range(len(head)):
            print(head[i])

    def sorted_insert(self, value):
        self.__value = value
        head = value
        if
