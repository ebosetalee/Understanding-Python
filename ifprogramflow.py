# name = input("Please enter your name: ")
# age = int(input("How old are you, {0}? ".format(name)))
# print(age)

# if age >= 18:
#     print("You are old enough to vote")
#     print("Put a number in the box")
# else:
#     print("Please come back in {0} years". format(18 - age))


print("Please guess a number between 1 and 10: ")
guess = int(input())

# if guess < 5:
#     print("Please guess higher")
#     guess = int(input())
#     if guess == 5:
#         #note the double equal to due to one creating a variable and double stating equation
#         print("Well done, you guessed it right")
#     else:
#         print("Sorry, you guessed wrong. Wanna guess again?")
#         guess = input()
#         if guess == "yes":
#             print("Guess a number between 3 and 7")
#             guess = int(input())
#             if guess == 5:
#                 print("Yayy!! you got it right!!!")
#             else:
#                 print("opps! Try again later")
#         elif guess == "no":
#             print("Thanks for trying, Try again later")
# elif guess > 5:
#     print("Please guess lower")
#     guess = int(input())
#     if guess == 5:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you guessed wrong")
# else:
#    print("You got it the first time")
# note that the symbol for not equal is !=
# instead of repetition of lines as in the code above, the code below can be used

if guess != 5:
    if guess < 5:
        print("Please guess higher.")
    else: # guess must be greater than 5
        print("Please guess lower.")

    guess = int(input())
    if guess == 5:
        print("Well done, you guessed it")
    else:
        print("Sorry, you have not guessed correctly.")
else:
    print("You got it the fist time")

#note the exercise
tree1 = "Oak"
tree2 = "Larch"

# add the code to compare the trees
if tree1 == tree2:
    print("The trees are the same")
else:
    print("The trees are different")
