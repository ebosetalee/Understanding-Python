#  Write a program that asks the user how many fibonacci numbers to generate and generates them.
numbers = int(input("How many times do you intend to generate the numbers? "))

num1 = 0
num2 = 1

count = 1
if numbers >= num2:
    print(num1)
    print(num2)
    while count < numbers:
        newNumber = num1 + num2
        print(newNumber)
        num1 = num2
        num2 = newNumber
        count += 1
else:
    print("Please type a number higher than {}".format(numbers))
