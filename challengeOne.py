name = input("What is your name? ")
age = int(input("How old are you? "))
print("My name is {0}. \nI am {1} years old.".format(name, age))
#I'm trying to type if age is less than 18 or greater than 31
if (age < 18) or (age > 31):
    print("Come back another time")
else: 
    print("Yayyy!! Welcome to the holiday!!! " + name)

# OR can be solved this way 

name = input("Please enter your name: ")
age = int(input("How old are you, {0}? ". format(name)))

# if 18 <= age < 31: or
if age >= 18 and age < 31:
    print("Welcome to club 18 - 30 holidays, {0}".format(name))
else:
    print("I'm sorry, our holidays are only for seriously cool people.")

# THE QUESTION
# write a small progam to ask for a name and an age
# when both values have been entered, check if the person
# is the right age to go on an 18 - 30 holiday (they must be
# above 18 and under 31).
# if they are, welcome them to the holiday, otherwise print 
# a (polite) message refusing them entry.

