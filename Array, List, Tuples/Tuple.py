# Tuples are used for grouping datas eg
coral = ['blue coral', 'staghorn coral', 'pillar coal', 'elkhorn coal']
# thats a tuple; its an immutable lists
print(coral[-4])
print(coral[1])

print(coral [1:4])
print(coral[::2])
# you can concatenate(add)and multiply(*) tuples 

# len() is used to calculate the content(length) in a string or tuple 
# this is done by passing the tuple as a parameter e.g len(coral) as seen below
print(len(coral))

# max() and min() is used with tuples composed of numeric items(integer and floats) to find the highest and lowest values
numbers = [14, 42, 34, 66, 74, 43, 56, 99, 37]
print(max(numbers))
print(min(numbers))
print(sum(numbers))
del numbers[2],numbers[4]
print(numbers)
#note that tuples cannot be modified(cannot add or remove) unlike list that if you type: 
# coral[0] = 'black coral' ; it changes blue coral to black coral
# however, we can convert a tuple to list by typing:
# list(coral) as well as converting list to tuple by: tuple(coral)
classes = ['Star', 'Shark', 'Storm', 'Shame', 'sleep'] 
print(classes)
