# When converting a decimal number to binary, you look for the highest power of 2 smaller thn the number
# and put a 1 in that column. You then tke the remainder and repeat the process with the next highest power - 
# putting a 1 if it goes into the remainder and a zero otherwise. keep repeating until you have dealt with all 
# powers down to 2 ** 0 (i.e. 1).
# 
# Write a program that requests a number from the keyboard, then prints out its binary representation.
# 
# Format string not accepted in this challenge.
# 
# The program should cater for numbers up to 65535; i.e (2 ** 16) - 1
# 
# Hint: You will need integer division (//), and modulo (%) to get the remainder.
# Also need ** to raise one number to the power of another:
# For example, 2 ** 8 raises 2 to the power of 8.
# 
# Optional extra, avoid printing leading zeros.
# 
# once the program is working, modify it to print Octal rather than binary.
a = int(input("Please type any number: "))
res=""
while (a > 0):
  c = a % 2
  d = a // 2
  res+=str(c)
  # print(c)
  a = d
print("The equivalent binary is " +  res[::-1])



# Solution by Instructor
powers = []
for power in range(15, -1, -1):
  powers.append(2 ** power)
print(powers)

x = int(input("Please enter a number: "))

# for power in powers:
#   print(x // power, end="")
#   x %= power
 
printing = False
for power in powers:
  bit = x // power
  if bit != 0 or power == 1:
    printing = True
  if printing:
    print(bit, end="")
  x %= power