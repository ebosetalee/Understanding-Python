# Example 1
file = open("fruits.txt","r")
for i in file:
  # i = [x.rstrip("\n") for x in i] #wrong it picks each word.
  print(i.rstrip("\n")) # correct.
file.close()

# Director's solution
# file1 = open("fruits.txt", "r")
# content = file1.read()
# file1.close()
# print(content)

# Example 2
# Please modify the code of the previous exercise so that instead of 
# printing out the lines in the terminal, it prints out the length of each line.
# for b in i:
#   print(len(b))
file = open("fruits.txt", "r")
content = file.readlines()
file.close()
for i in content:
     print(len(i.strip()))
