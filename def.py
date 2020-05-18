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