# still using sample.txt, we'll be explaining the writing to file using "w".
cities = ["Adelaide", "Alice Springs", "Darwin", "Melbourne", "Sydney"]

with open("cities.txt", "w") as city_file:
    for city in cities:
        print(city, file = city_file)
        # the file=city_file indicates that we want this to be a text file, the = is used for an assignment, i.e to provide a named 
        # argument in place of a file perimeter. Using the "w" not only writes to an existing file but creates a new file.
        # To use the flush command: flush=True

cities = [] 
with open("cities.txt", "r") as city_file:
    for city in city_file:
        cities.append(city)

print(cities)
for city in cities:
    print(city.strip("\n"))

# To see further explanation on .strip check File_strip.py

imelda = "More Mayhem", "Imelda May", "2011", (
    (1, "Pulling the Rug"),(2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))

with open("imelda.txt", "w") as imelda_file:
    print(imelda, file=imelda_file, flush=True)

with open("imelda.txt", "r") as imelda_file:
    contents = imelda_file.readline()

imelda = eval(contents) #eval isnt convenient when using external data.

print(imelda)
title, artist, year, tracks = imelda
print(title)
print(artist)
print(year)
# it is important to design code with securities and not leaving vulnerabilities in it