# it is possible to assign values to several variables at the same time.
# An exapmle of setting four variables to the same value:
a = b = c = d = 12
print(c)  

# You can also assign different values to multiple variables. e.g:
a, b = 12, 13
print(a, b)

a, b = b, a
print("a is {}".format(a))
print("b is {}".format(b))
# This shows the right hand assignment is evaluated first
# line 7 looks like a tuple that means we can pull out all the elements of a tuple in a single assignment. 
