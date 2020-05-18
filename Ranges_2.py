# # in python 2 ranges is implemented as a function''
# # but in python 3 ranges is built in type

# print(range(100))
# # note how it didnt print from 0-99 because the function for to loop through o list to make a list wasn't used.

# my_list = list(range(10))
# print(my_list)

# even = list(range(0, 10, 2))
# odd = list(range(1, 10, 2))
# print(even)
# print(odd)

# my_strimg = "abcdefghiijklmnopqrstuvwxyz"
# print(my_strimg.index('e'))
# # .index(with the word or letter in the list) was used to get the index representative also seen below 
# print(my_strimg[4]) # used [] if its a list of string and () for list on integers as nummber relates
# # to number and string to string.  

# small_decimal = range(0, 10)
# print(small_decimal)
# print(small_decimal.index(3))

# odd = range(1, 10000, 2)
# print(odd)

# print(odd[985])

# sevens = range(7, 1000000, 7)
# x = int(input("Please enter a positive number less than one million: "))
# if x in sevens:
#     print("{} is divisible by seven".format(x))
# else:
#     print("{} is not divisible by seven".format(x))
# #used to check a value that you parse using the in operator.

# print(small_decimal)

# my_range = small_decimal[::2]
# print(my_range)
# print(my_range.index(4))
# # this finds where 4 is as an index number
# print(my_range[4])
# # while this finds the index value of 4

decimals = range(0, 100)
print(decimals)

my_range = decimals[3:40:3]
print(my_range)

for i in my_range:
    print(i)

print("=" * 40)

for i in range(3, 40, 3):
    print(i)

print(my_range == range(3, 40,3))
# In the equality with ranges, what will the below code give us a true or false?
print(range(0, 5, 2) == range(0, 6, 2))
# it will print true because its not the value but the sequence of values are the same thus regardless of the value
# to understand this see:
print(list(range(0, 5, 2)))
print(list(range(0, 6, 2)))
# the tests of equality the result of the range not the actual numbers

# the stiff value of a slice can be negative.
r = range(0, 100)
print(r)

for i in r[::-2]:
    print(i)

print( "=" * 50)

for t in range(99, 0, -2):
    print(t)

print( "=" * 50)

print((range(0, 100)[::-2]) == (range(99, 0, -2)))

#look at this below:
for i in range(0, 100, -2):
    print(i)
    # nothing is printed because in the negative slice example, a negative step cause is a slice to be reversed
    # the same effect is obtained by specifying the a negative step in the range. this is seen 
    # but the start and end value must also be reversed otherwise the reading shows it starts from
    # 0 and moves in steps of -2 till it reaches 100. which is wrong.

m = range(0, 10)
for s in r[::-1]:
    print(s)