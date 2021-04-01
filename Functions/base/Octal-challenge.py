a = 450
print(0o702)
a = int(input("Please type any number: "))
res = ""
while (a > 0):
  c = a % 8
  d = a // 8
  res += str(c)
  # print(c)
  a = d
print("The equivalent octal is " + res[::-1])

# the Instructors Solution
powers = []
for power in range(15, -1, -1):
  powers.append(8 ** power)
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