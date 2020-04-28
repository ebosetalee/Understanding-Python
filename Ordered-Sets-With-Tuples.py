# Tuples is a term for an ordered set of data. which is similar to list.
# but the difference is they're immutable which means they can't be changed. Thus, attempting to append an item to a tuple will be an error.
# Lists are enclosed in square brackets [], is true but tuples enclosed in parentheses () is not true. becasue a comma , can be used to 
# separate the elements of a tuple, but the parentheses are only required when necessary to remove syntactic ambiguity. as seen below
t = "a", "b", "c",
print(t)
# this returned in brackets that signifies tuple
print("a", "b", "c")
# just returned the letters a b c which is an example of using parentheses
print(("a", "b", "c"))
# this returned a tuple
# Thus, print will also accept parameters followed by a comma, then you'd need to put brackets to print out a tuple
# use brackets as much as possible when creating a tuple.
# you can pass a comma seperated list of items to the print function and it'll print them on the same line.

welcome = " Welcome to my Nightmare", "Alice Cooper", 1975
bad = "Bad company!" " Bad company!!", 1974
budgie = "Nightlight", "Budgie", 1981
imelda = "More Mayhem", "Emilda May", 2011
metallica = "Ride the Lightning", "Metallica", 1984

print(metallica) 
print(bad)
print(metallica[0])
print(metallica[1])
print(metallica[2])
# Tuples are immutable so any action to change them would give an error.
# metallica[0] ="Master of Puppets" #run an error
# however, tuples support indexing and slicing which can be used to update particular entries
imelda = imelda[0], "Imelda May", imelda[2]
# being immutable means you cant change the contents of an object. but the change is done by reassagning the variable to a new object

# however a mutable as seen below:
metallica2 = ["Ride the Lightning", "Metallica", 1984] #list
print(metallica2)
metallica2[0] = "Master of Puppets"
print(metallica2)
# The difference is one is a list i.e mutable and the other a tuple that is immutable.
# Note however that the computer proceses / evaluates the right hand side assignment first before the left.

# tuples are favoured to list because:
# a. Dictionary key requires immutable objects 
# b. List is used to contain items of the same type i.e a real world list.
# c. to save a fixed item which shouldn't change 

# ANother example: known as unpacking the tuple
title, artist, year = imelda
print(title)
print(artist)
print(year)

#checking out while list may not work
metallica2.append("Rock")
print(metallica2)
# The append will add the new data to the end of the list not modify 
# the first thus giving it 4 variables to unpack 
# title, artist, year, style = metallica2 #has an error based on line 34
# print(title)
# print(artist)
# print(year)
# print(style)

#imelda.append("Jazz") #error
