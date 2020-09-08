# A string is a list. Thus, you can do to a string eveything you do to a list 
# e.g: list indexing([1: 5: 2]) and iteration(for loops).
# Ask the user for a string and print out whether the string is PALINDROME or not
# PALINDROME : is a string that reads the same forwards and backwards.

s = input("Please write any statement: ")
y = len(s)
print("There are " + str(len(s)) + " character(s)")
#  i dont know how to print a string backwards
print(s[: :-1])
# To print a string backwards use [::-1]