sims = [[2,4,6,-8],[-1, 1, 6, 7,], [100, 33, 6, 7]]
newList = []
# this is the single flat list 
# for y in sims:
#     for z in y:
#         newList.append(float(z))


for y in sims:
    newList.append([float(z) for z in y])
# this is the nested list comprehensions below of the above
newList = [[float(z) for z in y] for y in sims]
# this prints out a list of list by putting the second for loop first in a list bracket[] without the bracket,
# it will be a flat single list. 
print(newList)

# for start in newList:
#     for slow in start:
#         if slow % 2 == 0 and slow > 1:
#             print(slow)
# this is the nested list comprehensions below of the above:
sam = [slow for start in newList for slow in start if slow % 2 == 0 and slow > 1]
# the second for loop i.e for slow in start comes after as in the order above because we want a single 
# flat list and not a list of list as seen above. 
print(sam)