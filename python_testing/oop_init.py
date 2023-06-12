#!/usr/bin/python3

class Person:
    def __init__(self, name):
        self.name = name


    def say_hi(self):
        print('My name is', self.name)

p = Person('Victor')
p.say_hi()
