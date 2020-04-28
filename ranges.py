# Exercises: topic and lessons done in my laptop

# Experiment with different ranges and slices to get a feel for how they work.
# Remember that you can print the range as well as iterating through it to print.
# its values, to check that your ranges are what you expected.
# You may also want to include things like.

o = range(0, 100, 4)
print(o)
p = o[::5]
print(p)
for i in p:
  print(i)

# and see if you can work out what will be printed before running the program. if you 
# are unsure, use a for loop to print out the values of o to see why p returns what it does
a = range(10, 0, -2)
print(a)
for i in a:
  print(i)
b = a[::-2]
print(b)
# The slice [::-2] reverses the range, which was counting from 0 up to(but not including)
# 20, in steps of -2 and since the step multiplies each other, the value 4 will be used. 