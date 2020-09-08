# It also includes attributes, methods and constructors.
# in naming class, the first letter is in Capital letters.
class MyClass:
  x = 5

print(MyClass)

class Person:
    """ This class takes in an attribute of name and age, 
    and prints out an introduction in the introduce self"""
    def __init__(self, name, age):
        """This function using init stores variables in the 
        class called person"""
        self.name = name
        self.age = age
    def introduce_self(self):
        """ This function introduces the person"""
        print("My name is "+ self.name + 
    "\nI'm {} years old".format(self.age)) 


p1 = Person("John", 36)

print(p1.name)
print(p1.age)
print("My name is "+ p1.name + 
    "\nI'm {} years old".format(p1.age)) # This or
p1.introduce_self()

class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")
        # return function()

myobjectx = MyClass()
print(myobjectx.variable)
myobjectx.function() # calls the function method inside the class

# Object orientated programming aims to combine data and the processes that act to
# that data into objects which is called ENCAPSULATION e.g
a = 12
b = 4
print(a + b)
print(a.__add__(b))
# The results are the same, because they are defined the same way
# Everything in python is an Object.

# Obeject orientated programming uses classes and methods to provide objects that
# encapsulates both data and the functions that operate on that Data.
# Method is just another word for function. When funtion is part of a class in python,
# It is called Method.
# How does classes work in Python:  

class Kettle(object):

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True



kenwood = Kettle("Kenwood", 8.99)
print(kenwood.make)
print(kenwood.price)

kenwood.price = 12.75
print(kenwood.price)

hamilton = Kettle("hamilton", 14.55)
# Line 63 creates the instance of the kettle class with the name kenwood.
# Another instance created on line 70 named hamilton.
# A class is just a template for creating objects. Once a class is defned,
# we can create as many instances of that class as we want. Then we can 
# call their methods and access their variables.
#   
print("Models: {} = {}, {} = {}".format(kenwood.make, kenwood.price, hamilton.make, 
hamilton.price))
# When a variable is bound to an instance of a class, it is referred to as a
# data attribute 
# Another way to format string as in line 77 for data attributes are:
print("Models: {0.make} = {0.price}, {1.make} = {1.price},".format(kenwood, hamilton))
# Because kenwood and hamilton are objects, we can specify their attributes
# in the replacement fields. 
"""
Class: template for creating objects. All objects created using the same class will
have the same characteristics. In python, a class is the same as a type.
Objects: an instance of a class.
Instantiate: create an instance of a class.
Method: a function defined in a class.
Attribute: a variable to bound to an instance of a class. 
"""
# we'll notice something when we do
print(hamilton.on)
hamilton.switch_on()
print(hamilton.on)
# it prints: 
# False
# True. This can also be printed in another way
Kettle.switch_on(kenwood)
print(kenwood.on)
