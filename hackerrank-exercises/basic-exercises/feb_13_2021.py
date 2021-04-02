import math
# 1. Print the result of each of the following expressions:
print(6//5)  # = 1 Floor division - division that results into whole number adjusted to the left in the number line
# Divides and returns the integer value of the quotient. It dumps the digits after the decimal.

print(6/3)  # = 2.0
print(13.0/6)  # = 2.1666666666666665
print(9 % 3)  # = 0
print(3 % 9)  # = 3
print(8 % 3**2)  # = 8
print(2 % 6 // 3)  # = 0
print(18 // 4 // 2.0)  # = 2.0
print(18.0 / 4 // 2)  # = 2.0
print(-11.0 // (4 / 2))  # = -6.0

# 2. Write a program that calculates the total amount of a meal purchased at a restaurant. The program should ask the user
# to enter the charge for the food, then calculate the amounts of a 15 percent tip and 9 percent sales tax. Display the amount of tip, tax, and the total.


def total_meal():
    food_charge = int(input("How Much did your food cost? "))
    print("Food:       {}".format(food_charge))
    tip = food_charge * (15/100)
    print("Tip of 15%: {}".format(tip))
    tax = food_charge * (9/100)
    print("Tax of 9%:  {}".format(tax))
    total = food_charge + tip + tax
    print("Total Meal: {}".format(total))


total_meal()

# 3. Write a program that asks the user to enter the radius of a circle. The program should calculate and display the area and circumference of the circle using πr2 for the area and 2πr for the circumference.
# Hint: You can either use 3.14159 as the value of pi (π), or add the statement "import math" to the start of the program and then use "math.pi" wherever you need the value of pi in the program.


def calc_circle():
    radius = int(input("What is the radius of the circle? "))
    circumference = (2 * math.pi) * radius
    area = math.pi * (radius ** 2)
    return "Radius: {0}, Area: {1:.2f}, Circumference: {2:.2f}".format(radius, area, circumference)


print(calc_circle())

"""
4. When a bank account pays compound interest, it pays interest not only on the principal amount that was deposited into the account, but also on the interest that has accumulated over time. 
Suppose you want to deposit some money into a savings account, and let the account earn compound interest for a certain number of years. The formula for calculating the balance of the account after certain number of years is:
   𝐴 = 𝑃 (1 + 𝑟 / 𝑛)**𝑛𝑡
The terms in the formula are:
A is the amount of money in the account after the specified number of years. 
P is the principal amount that was originally deposited into the account.
r is the annual interest rate.
n is the number of times per year that the interest is compounded.
t is the specified number of years.

Write a program that makes the calculation. The program should ask the user to input the following:
The amount of principal originally deposited into the account
The annual interest rate paid by the account
The number of times per year that the interest is compounded (For example, if interest is compounded monthly, enter 12. If interest is compounded quarterly, enter 4.)
The number of years the account will be left to earn interest
"""

def balance():
    p = int(input("What is the principal amount? "))
    r = int(input("What is the annual interest rate? "))
    n = int(input("What is the number of times per year that the interest is compounded? "))
    t = int(input("What is the specified number of years? "))
    nt = n * t
    balance_total = p * ((1 + (r / n)) ** nt) 
    return "The Balance of Account is {}".format(balance_total)
print(balance())

