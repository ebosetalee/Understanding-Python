# write a program to print the LCM of two inputted numbers
a = int(input("Type a number "))
b = int(input("Type another number "))

if (a < b):
    lowest_number = a
else:
    lowest_number = b
common_multiple = int(a * b)
while lowest_number <= common_multiple:
    if (lowest_number % a == 0 and lowest_number % b == 0):
        print("LCM is {}".format(lowest_number))
        # break
    lowest_number = lowest_number + 1
        


array = [1,2,3,4]
