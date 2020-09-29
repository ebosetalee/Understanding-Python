# ord() is used to get the ascii values of any character.

ab = "a"
print(ord(ab))
print()

alpha = "abcdefghijklmnopqrstuvwxyz"

for letter in alpha:
    print(str(ord(letter)))

ants = None
print(ants)
if ants == None:
    print("None")
    ants = {}
ants[5] = ["space"]
print(ants)
ants[5].append("slope")
print(ants)

val = "Jasmine Smith"
addd = 0
for char in val:
    addd += ord(char) 
print(addd)
print(addd % 100)
print(id(val))