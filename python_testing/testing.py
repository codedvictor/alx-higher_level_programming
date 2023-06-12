#!/usr/bin/python3

class Robot:
    pass
if __name__ == "__main__":
    x = Robot()
    y = Robot()
    y2 = y
    print(y == y2)
    print(y == x)
    x.name = "Marvin"
    x.build = 1967
    y.name = "marvel"
    y.build = 1990
    print(x.__dict__)
    print(y.__dict__)
Robot()

"""method outsie class"""
def hi(obj, obt):
    print("Hi " + obj.name + ", My name is " + obt.name)
class Robot1:
    pass
x1 = Robot1()
y1 = Robot1()
y1.name = "Victor"
x1.name = "John"

hi(x1, y1)


