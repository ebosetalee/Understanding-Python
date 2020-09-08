# Ask the user for a number. Depending on whether the number is even or odd, 
# print out an appropraite message to the user.

# number = int(input("Please pick a number "))
# if number % 2 == 0:
#     print("Thank you for choosing an even number. Take care")
# else:
#     print("You choose an odd number. Yayyyy!!!!")

# # Extras:
# # 1. If the number is a multiple of 4, print out a different message.
# if number % 4 == 0:
#     print(''' 
#     You also chose a multiple of 4,
#     we can't let you go just yet...
#     you're a special breed of 4's
#     Now we can let you go.
#     Have fun!!!!''' )

# 2. Ask the user for the numbers: one number to check (call it num) and
# one number to divide by (check). If check divides evenly into num, tell
# that to the user. If not, print a different appropriate message.

num = int(input("Please type another number "))
check = int(input("Please type a different number "))

if (check % num == 0) or (num % check == 0):
    print("The numbers divide each other")
else:
    print("The numbers are against each other")