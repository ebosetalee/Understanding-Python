import re

txt = "The rain in Spain"
x = re.sub("n", "9", txt)
print(x)

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())

s = input("type a letter ").upper()
if re.search("[A-Z]{2}|[0-9]|\W", s):
    print("Found a match.")  
else:
    print("No match.")

validation = re.search("^([a-zA-Z]|!)$", s)
if validation:
    print("yayyyy")
else:
    print("one letter or !")

males = ["bayo", "simi", "truce!4", "smile!#"]
male = "truce!$"
stop = re.search("[a-zA-Z]\w+", male)
rain = stop.group()
print(stop)
print(rain)

m = 140
total = 0
for i in range(m):
    total += (m-i)
    print(total)