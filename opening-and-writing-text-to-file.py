file = open("examples.txt", "w")
# open not only opens an exisiting file but creates a non existing file too. and w is for write.
file.write("Line 1")
file.close()
file = open("examples.txt", "w")
file.write("Line 2") # you'll only get Line 2 as ouput as W is not an appending method.
# thus, impossible to add multiple lines using the write method, thus need to be done in one session
file = open("examples.txt", "w")
file.write("Line 1\n")
file.write("Line 2") # added \n to create a new line to seperate the values
file.close()

# having 20 lines, the need to use the for loop to have them instead of write method 20 times.
file = open("examples.txt", "w")
l =  ["line 1","Line 2", "Line 3"]
for item in l:
  file.write(item + "\n")
file.close()

# Appending to a file
file = open("examples.txt", "a")
file.write("Line 4")
file.close()

# to read and write use r+ (R plus) but places the pointer at the begining of the test.

# to write and read w+ but it overwrites the existing file

# a+ places the pointer at the end of the file.

# WITH STATEMENT
# it lets write cleaner code, for quick writing and make sure the file is closed without writing close.

with open("example.txt", "a+") as files:
  files.seek(0) # not important as the pointer is at the end.
  files.write("\nLine 7")