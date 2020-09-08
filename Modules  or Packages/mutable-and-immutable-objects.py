# immutable objects means it can't be changed.

# The following immutable types are built into Python: int; float; bool - which is True or False; 
# a subclass of int; string or str - which is a string; tuple; frozenset and bytes.

# id returns an identity of an object; It must be "guaranteed to be unique and constant for this 
# object during it lifetime

result = True
another_result = result
print(id(result))
print(id(another_result))

# if bool values could be changed, then changing the values should mean that the ID doesn't change:
result = False
print(id(result))
# if you look closely, we didnt change the value of true but rebound result to a new value - False

print("=="* 40)

# A  mutable object is one whose value can be changed. 
# Python has the following mutable objects built in: list, dict,set and byte array.

shopping_list =["milk",
                "pasta", 
                "eggs",
                "spam",
                "bread",
                "rice"   
                ]

another_list = shopping_list
print(id(shopping_list))
print(id(another_list))

shopping_list += ["cookies"]
print(shopping_list)
print(id(shopping_list))
# the ID remains unchanged, and that's because lists are mutable and 
# Python was able to add a newitem to the end of the list, without creating a new list.
print(another_list)

a = b = c = d = e = f = another_list
# this bound more names to the list and we can use any name to call the list.
print(a)

print("Adding cream")

b.append("cream")

print(c)
# we'll see that cream is added to the list regardless of the name used to call it 
print(d)

print(id(a))
print(id(b))
print(id(c))
print(id(another_list))
#we see they have the same id