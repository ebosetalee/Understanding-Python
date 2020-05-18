print("\n\n----------------------------------------------------------------------------\n\n")
numbers = [1,2,3,4]

# print numbers
print(numbers)

# prints the first number 
print(numbers[0])

#print each item in numbers seperately
for x in numbers:
    print(x)

# add new items to array
numbers.append(9)
print(numbers)

print(numbers[-2])

# change 3 to 10
numbers[2] = 10

print(numbers)

addition = 0
for item in numbers:
    addition = addition + item
print(addition)


x = 24 % 4
print(x)