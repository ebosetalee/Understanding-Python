# with two lists below, write a program that returns a list that contains
# only the elements that are common between the lists without duplicates.
# make sure the program works on two lists with different sizes. 

amp = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
ball = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# for item in amp:
#     for elem in ball:
#         if item in elem:
#             print(item)           
# x = 10
# x in ball:
#     print(x)
# clean = []
# for star in amp:
#     if star in ball and star not in clean:
#         clean.append(star)
# print(clean)

clean = set([star for star in amp if star in ball])
print(clean)

# Remember when you need to add/ modify to a list or array use .append()
# Extras:

# 1. Randomly generate two lists to test this

# answer = range(1, 100, 2)
# braces = range(23, 134, 3)
# crest = []
# for status in answer:
#     if status in braces and status not in crest:
#         crest.append(status)
# print(crest)

# 2. Write this in one line of python code
#  This is done using list comprehension 
#  e.g: years_of_birth = [1990, 1991, 1990, 1990, 1992, 1991]
#  ages = [2014 - year for year in years_of_birth]
# Instead of: ages[]
#  for year in years_of_birth:
   #  ages.append(2014 - year)
#    note that what ought to be in the for/if loop,(.append) comes before them in list comprehensions
#  while for comes before if
# The idea of list comprehensions is to condense the for loop and list appending into one simple line.

# SOLUTION:
