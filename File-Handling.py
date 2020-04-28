file =  open("example.txt", "r") 
type(file) #shows the type of the variable.
content = file.read() # this places the pointer at the end 
print(content) # prints the content as a string
contents = file.readlines() # makes the contents a list   
print(contents) # prints an empty list because the from the pointer at the end there's no data.
file.seek(0) #this places the pointer back to the beginning and used to get control over files.
contents = file.readlines()
print(contents)
contents = [i.rstrip("\n")for i in contents] # a list comprehension with rstrip which removes a particular thing from a variable.
print(contents)
file.close() # close the file in order for it to save the modifications made to the file.
