# str() for sting formatting as the variable in the bracke is a number.
age = 20
print("My age is " + str(age) + " years" )

# Another method is called the replacement fields
# Replacement is known as making use of {} then .format(variable name) e.g
print("My age is {0} years".format(age))

# it is useful when contaneting alot of strings and integal
print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7} ".format(31, "January", "March","May", "July", "August", "October", "December"))

print("There are {0} days in {1}, {2}, {3} and {4} .".format(30, "April", "June", "September", "November"))

print("""Each month has the following days: \nJanuary: {3}; \nFebruary: {0} or {1} every leap year; \nMarch: {3}; \nApril: {2}; \nMay: {3}; \nJune: {2}; \nJuly: {3}; \nAugust: {3}; \nSeptember: {2}; \nOctober: {3}; \nNovember: {2} and \nDecember: {3}.""".format(28, 29, 30, 31))

# string formatting operator deprecated(wasn't used) in python 3
# using %d for digit and %s for sting
# note that there's a comma after %s and there's a bracket because of using alot of figures to be replaced
print("\nMy age is %d years" %age)

print("My age is %d %s, %d %s" %(age, "years", 6, "months"))

for i in range(1, 12):
    print("No. %2d is squared is %3d and cubed is %4d" %(i, i ** 2, i ** 3))

print("Pi is appoximately %12.4f" %( 22 / 7))
# note that the % sign shoud'nt be used in python3 
# note also that the number before d is used for precision

for i in range(1, 12):
    print("No. {0:2} is squared is {1:3} and cubed is {2:4}".format(i, i ** 2, i ** 3))

# another way of doing it is:
for i in range(1, 12):
    print("No. {0:2} is squared is {1:<3} and cubed is {2:<4}".format(i, i ** 2, i ** 3))


print("Pi is appoximately {0:12.4}".format( 22 / 7))

#note that the use of numbers in replacement fields is optional e.g
for i in range(1, 12):
    print("No. {:2} is squared is {:3} and cubed is {:4}".format(i, i ** 2, i ** 3))
#however, where you need to use it more than once then specify number.
