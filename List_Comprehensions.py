# combs = [(x,y) for x in [1,2,3] for y in [3,1,4] if x != y]
# print(combs)
# #  is the same as:
# c = []
# for a in [1,2,3]:
#     for b in [3,1,4]:
#         if a != b:
#             c.append((a,b))
# print(c) 
# Another example as explained in list overlap, if the expression is tuple

vec = [-4, -2, 0, 2, 4]
# create a new list with the values doubled
f = [d*2 for d in vec]
print(f)

sims = [[2,4,6,-8],[-1, 1, 6, 7,], [100, 33, 6, 7]]
newList = [[float(z) for z in y] for y in sims]
print(newList)
for start in newList:
    for slow in start:
        if slow % 2 == 0 and slow > 1:
            print(slow)
 
# sam = [slow for start in newList for slow in start if slow % 2 == 0 and slow > 1]
# print(sam)
# filter the list to exclude negative numbers
g = [e for e in vec if e >= 0]
print(g)

# create a list of 2- tuples like (number, square)
# the tuple must be parenthesized i.e (), otherwise an error is raised
h = [(i, i**2) for i in range(6)] 
print(h)

# flatten a list using a listcomp with two 'for'
j =[[1,2,3], [4,5,6], [7,8,9]]
# k = [num for elem in j for num in elem]
# print(k)

# Note there's nested list comprehension check the next file
# EXERCISES:
# Write one line of python code that takes this saved list l and
# makes a new list that has only the even elements of this list in it.

l = [1, 4, 9, 16, 25, 49, 64, 81]
m = [n for n in l if n % 2 == 0] 
print(m)
import random
for elem in l:
    print(elem)
k = elem % 2 == 0
o = random.sample(l,(k))
print(o)
# this doesnt work that way as k is foe length of element to be printed