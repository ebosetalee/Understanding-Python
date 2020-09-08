# Take a list and write a program that prints out all the
# elements of the list that are less than 5.
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for x in a:
    if x <= 5:
        print(x)

# Extras:
# 1. Instead of printing the elements one by one, make a new list that has all the elements
# less than 5 from this list in it and print out this new list.
y = [1,1,2,3,5]
print(y)

# 2. Write this in one line of python
print([1,1,2,3,5])

# 3. Ask the user for a number and return a list that contains only elements from the
# original list a that are smaller than that number given by the user.
used = int(input("please type a number: "))
res = []
for oop in a:
    if oop < used:
        res.append(oop)
print(res)
