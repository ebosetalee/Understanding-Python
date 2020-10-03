# a for loop is done in the following
#for [iterating variable] in [sequence]:
#   [do something]
# three important things start( states the integer value at which the 
# sequence begins, if this is not included, starts at 0)
# stop(is always required and is the integer that is counted up to but not included
# step(sets how much to increase (or decrease where it is negative) the next iteration, default is 1)
# range(stop) as seen below
for i in range(6):
    print(i)

# range(start, stop) as seen below
for i in range(14,21):
    print ("i is now {} ".format(i))

# range(start, stop, step) as seen below
for i in range(0, 15, 3):
    print(i, end = ', ')

# step can be negative as seen below but the start and stop be changed accodingly as seen belo
for i in range(100, 0, -10):
    print(i)

# seperators
for i in range(5):
    print(1, 2, 3, sep=":")

sharks = ['hammerhead', 'Great White', 'dogfish', 'frilled', 'bullhead']
for x in sharks:
    print(x)
list(sharks)
print(sharks, end = '\n')
tuple(sharks)

# note that ", end = '\n'" doesnt work for list or tuple only strings
sharks.append('star')
print(sharks, end = '\n')
for x in sharks:
    print(x)
for item in enumerate(sharks):
    print(item)

# you can combine list, strings and tuple using range() to add items to a list or tuple. eg: .append
for item in range(len(sharks)):
    sharks.append('star')
print(sharks)


# however, you can use a for loop to construct a list fom scratch:
integers = [5]
for i in range(10):
    integers.append(i) 
print(integers)

print("Please guess a number: ")
lclm = [7]
for x in range(20):
    lclm.append(x)
print(lclm)

# number = [input("Please guess a number: ")]
# list(number)
# lcm = []
# for x in range(10):
#     lcm.append(x)
#     for item in x:
#         x.append(number)
# number.append(lcm)
# # # number.append(lcm)
# for item in number:
#     print(item,end='\n')

# iterate through strings
sammy = 'sammy'
for m in sammy:
    print(m)

sammy_shark = {'Name': 'Sammy', 'Animal': 'Shark', 'Colour': 'Blue', 'Location': 'Ocean'}
for k in sammy_shark:
    print(k + ': ' + sammy_shark[k])

# # this isn't working, why?
# use append or update to add to a dict. if using append add the key value
sammy_shark.update({'Street': 'Rocks'})
# sammy_shark ["Street"] = "Rocks" 
# print(sammy_shark)

for x in sammy_shark:
    print(x + ': ' + sammy_shark[x])

# Nested loop is a loop that occur within another loop; as seen below:
# for [first iterating variable] in [outer loop]: #outer loop
#   [do something] # optional 
#   for [second iterating variable] in [nested loop]: # Nested loop
#       [do something] eg:

num_list = [1, 2, 3]
alpha_list = ['a', 'b', 'c']
for numbe in num_list:
    for letter in alpha_list:
        print(numbe,letter) 
        #  this is used for iterating through items within list omposed of ists

# if you use one for loop, the progam will output each internal list as an item:
list_of_lists = [['Hammerhead', 'Great White', 'Dogfish'], [0, 1, 2], [9.9, 8.8, 7.7]]
for x in list_of_lists:
    print(x)
for x in list_of_lists: 
    for item in x:
        print(item)
        
# len stands for length which produces a length of strings
# number = "9, 223, 372, 036, 854, 775, 807"
# for i in range(0, len(number)):
#     print(number[i])
# where you have this len(number)-1) the -1 is added to miss the last number

number = '9,223,372,036,854,775,807'
cleanedNumber = ''

# this is used to ignore the comas and print what is found in 0123456789
for char in number:
        if char in '0123456789':
                cleanedNumber += char


newNumber = int(cleanedNumber)
print("The number is {}".format(newNumber))

for state in ["not pinin", "no more", "a stiff", "bereft of life"]:
        print("This parrot is " +  state )
        # or print("This parrot is {}".format(state))
# a range is a sequence of values which states the start and end

for i in range(0, 100, 5):
        print("i is {} ". format(i))


# a for loop can be nested as seen below
for l in range(1,13):
        for m in range(1,13):
                print("{1} times {0} is {2}".format(l, m, l*m))
        print("=====================")        
