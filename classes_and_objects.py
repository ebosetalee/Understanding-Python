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