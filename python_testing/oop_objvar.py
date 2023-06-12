#!/usr/bin/python3

class Robot:
    """class representation with a name """

    population = 0 #a class variable, counting the number of robots

    def __init__(self, name):
        """initialize the data Method"""
        self.name = name
        print("Initializing {}".format(self.name))
        #new person is created in class robot

        Robot.population += 1 #adds to the population

    def die(self):
        """I am dying"""
        print("{} is being destroyed".format(self.name))

        Robot.population -= 1 #Remove from the population

        if Robot.population == 0:
            print("{} is the last one".format(self.name))
        else:
            print("There is still {:d} working".format(Robot.population))

    def say_hi(self):
        """Greeting by robot.
        They can do that"""

        print("My handler call me {}".format(self.name))

    @classmethod
    def how_many(cls):
        """Print the current population."""
        print("We have {:d} robot".format(cls.population))

droid1 = Robot("IG VK1")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("IG VK2")
droid2.say_hi()
Robot.how_many()

print("\n We are here to do the hard things \n")

droid1.die()
droid2.die()

Robot.how_many()
