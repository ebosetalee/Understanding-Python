# Question:
# Create a program that asks the user to enter their name and their age. 
# Print out a message addressed to them that tells them the year that they will turn 100 years old.

name = input("What is your name? ")
age = int(input("How old are you? "))
today = int(input("what is the year of your last birthday "))

if age < 100:
    x = 100 - age
    year = x + today
    print("{}, in {} years time in {} you will be 100 years old. Enjoy your years!".format(name, x, year))
else:
    print("Please tell us your age. Thank you")


# Extras:
# 1.Add on the program by asking the user for anothe number and printing out that many
# copies of the previous message
# 2. Print out that many copies of the previous message on separate lines.

new = int(input("How many times do you want me to reprint? "))
for y in range(0,new):
    print("{}, in {} years time in {} you will be 100 years old. Enjoy your years!".format(name, x, year))

# Another way to solve it:
# remove the variable "today" and the if function using while 