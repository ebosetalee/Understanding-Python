a = int(input("Type a number "))
b = int(input("Type another number "))
c = int(input("Type a third number "))

if (a < b) and (a < c):
    lowest_number = a
elif (b < a) and (b < c):
    lowest_number = b
else:
    lowest_number = c
common_multiple = int(a * b * c)
print("Common multiple of {}, {} and {} is".format(a, b, c), end = ' ')
while lowest_number <= common_multiple:
    if (lowest_number % a == 0 and lowest_number % b == 0 and lowest_number % c == 0):
        print(lowest_number, end = ', ')
    # lowest_number = lowest_number + 1
    lowest_number += 1
print('.')        