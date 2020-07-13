# A function is a structuring element to group a set of statements so they can be utilized more than once in
# a program. A function in Python is defined by a "def" statement. That looks like this: 
# def function-name(parameter list):
#     statements, i.e the function body
# The parameter list consists of none or more parameters. Parameters are called arguments, if the function is
# called. The function body consists of indented statements. The function body gets executed every time the 
# function is called.Function bodies can contain one or more return statement. They can be situated anywhere in 
# the function body. A return statement ends the execution of the function call and "returns" the result.
unit = 20
score = 56
def gpa():
    results = score / unit
    print(results)
gpa()

# More on defined functions:
def reqarg(str, num):
    reqarg ("hello", 12)

# in a simple sentence, def function is used instead of repeating the code
import datetime
# print the current time
def print_time():
    print("task completed")
    print(datetime.datetime.now())
    print() # this just prints an empty line.

# OR

# from datetime import datetime
# # print the current time
# def print_time():
#     print("task completed")
#     print(datetime.now())
#     print()

name = "Susan"
print(name)
print_time() 

for x in range(10):
    print(x)
    print_time()
print_time()

print("-" * 40)

# Using parameter (task_name is the parametr in this code):
def prints_time(task_name):
    print(task_name)
    print(datetime.datetime.now())
    print()

firsts_name = "Susan"
print(firsts_name)
prints_time("first name assigned") 

for xy in range(10):
    print(xy)
prints_time("loop completed")

# Exercise:
# Convert the code below using functions:

# first_name = input("Enter your First name: ")
# first_name_initial = first_name[0:1]

# last_name = input("Enter your Last name: ")
# last_name_initial = last_name[0:1]

# print("Your Initials are: "+ first_name_initial + last_name_initial)

# SOLUTION:

# def get_initial(names):
#     initial = names[0:1]
#     return initial

# first_name = input("Enter your First name: ")
# first_name_initial = get_initial(first_name)

# last_name = input("Enter your Last name: ")
# last_name_initial = get_initial(last_name)

# print("Your Initials are: "+ first_name_initial + last_name_initial)

# OR  a shorter code:
def get_initial(names):
    initial = names[0:1].upper()
    return initial

first_name = input("Enter your First name: ")
last_name = input("Enter your Last name: ")

print("Your Initials are: "+ get_initial(first_name) + get_initial(last_name))

# conditions can be used in def function e.g "if":
def get_initials(named, force_uppercase):
    if force_uppercase:
        initials = names[0:1].upper()
    else:
        initials = names[0:1]
    return initials

first_names = input("Enter your First name: ")
first_name_initials = get_initials(first_names, True)
print("Your Initials are: "+ first_name_initials)

email = input("Enter your Email Address: ")
email_initial = get_initials(email)
print("Your Email Initials are: "+ email_initial, False)
# Named notation works well when the parameters are alot or someone is reading your code