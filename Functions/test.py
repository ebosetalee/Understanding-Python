# greeting = "Hello"
# name = input("Please enter your name: ")
# print(greeting + " " + name)
# #
# software = "My unavoided cousin \nraise his voice \noh damn \nJane said it's terrible"
# print(software)

# slim = "1\t2\t3\t4\t5\t6"
# print(slim)
# used ctrl + slash for hashtags

# print("The pet shop owner \"No, no, no! 'e's uh;.... he's resting\"")
# print('The pet shop owner "No, no, \'e\'s uh,... he\'s resting" oh ok')


# a = 12
# b = 3
# print(int(a / b))
# print(a//b)

# % means remainder

# print(a % b)


# parrot = "Norweigian Blue"
# print(parrot[-1])
# print(parrot[3])
# print(parrot[0])

# print(parrot[0:6])

# today = "Saturday"
# print("sat" in today)
# print("day" in "today")
# print("ur" in today)
# print("lim" in "shallowlim")


a = [5, 10, 15, 20, 25]
b = a[0], a[-1]
# list(b)
print(b)
c = []
c.append(b)
print(c)

def lends(a):
    return(a[0], a[-1])
print(lends(a))