# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell
# them whether they guessed too low, too high, or exactly right. Keep the game going till the user types "exit"
# Keep track of the guesses and print it out
import random

computer = random.randint(1,9)

# x = 0
# while x < 9:
#     guess = int(input("Please guess a number between 1 and 9: "))
#     x += 1
#     if guess == computer:
#         print("You guessed right yay!!!!")
#         print("You Guessed {} tries".format(x))
#         break
#     elif x == 5:
#         stop = input("If you wish to stop type exit: ")
#         if stop == "exit":
#             print("Thanks for trying")
#             break
#         else: 
#             continue
#     elif guess < computer:
#         print("You guessed a lower number, please try again")
#     else:
#         print("You guessed a higher number, please try again")  

# Another way to solve it
number = computer
guess = 0
count = 0

while guess != number and guess != "exit":
    guess = input("What's your guess? ")
    if guess == "exit":
        break
    guess = int(guess)
    count += 1
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("You got it right! and it only took you {} tries".format(count))