# Create a program that asks the user for a number and then
# prints out a list of all the divisor of that number

num1 = int(input("Please type a number above 20 "))
# sims = 0
# THIS DIDNT WORK
# while True: £ note the capital letter T
#     sims += 1
#     if num1 % sims == 0:
#         sims += 1
#     print(sims)
# break  
x  = range(1,num1)
#  THIS WORKS
# for elem in x:
#     if num1 % elem == 0:

#         print(elem)

#  OR

sims = 1
#  YAYYYY THIS WORKS TOO
while sims <= num1:
    if num1 % sims == 0:
        print(sims)
    sims += 1