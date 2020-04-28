# Sets and dictionaries are unordered collections having no duplicates in it.

fruit = {"orange": "a sweet, orange, citrus fruit",
  "apple": "Good for making Cider", 
  "lemon": "A sour, yellow citrus fruit",
  "grape": "A small, sweet fruit growing in bunches", 
  "lime": "A sour, green citrus fruit"}
# Note the parenthesis used {}
# Also note that after each variable that includes a key before, there's a comma ,
print(fruit)
print(fruit["lemon"])

bike = {"make": "Honda", "model": "250 dream", "colour": "Red", "engine Size": 250}
print(bike)
print(bike["engine Size"]) # or engine_size (no difference)

# You can append (add) to a dictionary
fruit["pear"] = "An odd shaped apple"
# Note the key in brackets []
print(fruit)
# however, assigning a value to an existing key will switch the values rather than having another entry.
fruit["lime"] = "Great with tequila"
print(fruit)

# del commnd to remove an item or the whole dictionary.
del fruit["lemon"]
print(fruit)

# this deletes the dictionary without entiring removing it
fruit.clear()
print(fruit)

while True:
  dictKey = input("Please type a fruit: ")
  if dictKey == "quit":
    break
  descrip = fruit.get(dictKey)
  print(descrip) 
# prints none if the key doesn't exist and not error

while True:
  dictKey = input("Please type a fruit: ")
  if dictKey == "quit":
    break
  if dictKey in fruit: #also use (in) to check if the key typed is in the dictionary
    descrip = fruit.get(dictKey) # use .get to retrieve the dictionary
    print(descrip)
  else:
     print("We don't have a " + dictKey) 
# the alternative is to use a default value to return if the key doesnt exit, as seen below:
#   descript = fruit.get(dictKey, "we don't have a " + dictKey) use this if the key doesnt exist
  # there is has_key method used to check if the key is in the dictionary, seen below:
  # fruit.has_key(dictKey) #however, it is a python 2 method not seen in python 3.
  print(descript) 

# Iteration (the order can change in every execution)
for snack in fruit:
  print(fruit[snack])

# Note: Hash is a one-way function used in cryptography or calculating check sums or store passwords in d3atabase

# access the value as its iterable (hash can always be used)
for i in range(10):
  for snack in fruit:
    print(snack + " is " + fruit[snack])
  print("-" * 40) #(this makes it come out in the same order unending, however if you add or delete it can chage the order) 
# also note that it changes based on the time the dictionary is created i.e the run

# If you want to have a particular order or to use dictionary in an ordered number which is useful if you want an orderd result
# What you need is to create a list from the dictionary keys, sort the list an iterate over the list to display the result. As seen below:

# Ordered or sorted list to iterate through
ordered_keys = list(fruit.keys()) #turns a list of all the keys
ordered_keys.sort() #OR
ordered_keys = sorted(list(fruit.keys())) #this line sorts the list as its created
for f in ordered_keys:
  print(f + " = " + fruit[f]) # the keys method is used inorder to sort the keys first before printing (sorted keys method) OR

for f in sorted(fruit.keys()):
  print(f + " = " + fruit[f]) #note.keys is used because of the sorted function, to sort the values if not use "for f in fruit:"

# OR the Values command:

for val in fruit.values():
  print(val) #They all help print in alphabetical order but val doesn't print the keys 

print ("-" * 40)
# instead of val use this:

for key in fruit:
  print(fruit[key])

print(fruit.keys())

print(fruit.values()) 
# They both return list like object; the keys method returns a dictkey object and values return a dictvalue object


print("-" * 40)

# fruit_keys = fruit.keys() creating a different value
print(fruit_keys)

fruit["tomato"] = "not nice with ice cream"
print(fruit_keys)

print(fruit)
print(fruit.items()) # this is a dynamic view object that consist of key value and tuples.

# we can produce a tuple from fruit.items using:
f_tuple = tuple(fruit.items())
print(f_tuple)

# with tuple you can use it the same way you use tuple e.g:
for snack in f_tuple:
  item,description = snack
  print(item + " is " + description)

# python is easy to move from dict to tuple and vice versa eg.
print(dict(f_tuple))
# This shows how a dictionary can be created from the tuple

# Another string method is Join and string is immutable: this means is not all efficient to cancatenate string in a loop.
# Every time you cancatenate a string to an existing string, a new string has to be created and if its done in a loop it is expensive and slow.
# The String join method is there to help which takes a sequence and produce a new string from it and seperated from the string the join was called upon 
# Check file "string join method"