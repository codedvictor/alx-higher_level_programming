#!/usr/bin/python3
""""Write a class MyList that inherits from list"""


class MyList(list):
    """my list from list superclass"""
    
    def print_sorted(self):
        cp_list = self.copy()
        cp_list.sort()
        print(cp_list)
