# age = int(input("How old are you? "))
# # we could type this way 
# # if age >= 16 and age <= 65: add brackets like
# # if (age >= 16) and (age <= 65):or
# # if 16 <= age <= 65: or
# # if 15 < age < 66:
# #     print("Have a good day at work!")
# # Using and means both conditions have to be true where as using or as seen below means either condition is true for the statement to print
# if (age < 16) or (age > 65):
#     print("Enjoy your free time!")
# else:
#     print("Have a good day at work!")

# # Note in the new codes below false is 0 and true is 1
# x = input("Please enter some text ")
# if x:
#     print("You entered '{}'".format(x))
# else:
#     print("You did not enter anything")

# print(not False)
# print(not True)   

# since not False will be true and not True is False. As seen below

# age = int(input("How old are you? "))
# if not(age < 18):
#     print("Congratulations! You are old enough to vote.")
#     print("Please put an X in the box.")
# else:
#     print("Please come back in {0} years.".format(18 - age))

parrot = "Norwegian Blue"

letter = input("Enter a character: ")

# if letter in parrot:
#     print("Give me an {} , Dave".format(letter))
# else:
#     print("I don't need that letter dear")

# however, we're using not so:
if letter not in parrot:
    print("I don't need that letter dear")
else:
    print("Give me an {} , Dave".format(letter))