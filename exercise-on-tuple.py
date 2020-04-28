# Given the tuple below that represents the Imelda May album "More Mayhem", write
# code to print the album details, followed by a listing of all the tracks in the album
# 
# Indent the tracks by a single tab stop when printing them (remember that you can pass
# more than one item to print function, separating them with a comma).

imelda = "More Mayhem", "Imelda May", 2011, (
  (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))
print(imelda)

# sample solution
title, artist, year, tracks = imelda
print(title)
print(artist)
print(year)
for song in tracks:
  track, title = song
  print("\tTrack number {}, Title: {}".format(track, title))

# once you've represented your album collection as tuples,
# We'll destroy all the tuples in the list, or store them in another tuple.
# 
# Since a list is mutable and a tuple is immutable,
# Then, if a tuple contains a list or a list containing individual tuples
# though the tuple cannot be changed, 
# but the contents of the list can be changed. e.g
imeldas = "More Mayhem", "Imelda May", 2011, (
    [(1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz")])
print(imeldas)

imeldas[3].append((5, "All For You"))

title, artist, year, tracks = imeldas
tracks.append((6, "Eternity"))
print(title)
print(artist)
print(year)
for songs in tracks:
  track, title = songs
  print("\t Track number {}, Title: {}".format(track, title))

products = (("No. 5", "perfume", "Chanel"),
  ("Inflallible", "cosmetic", "L'Oreal"),
  ("Poison", "Perfume", "Dior"))

for product in products:
  name, product_type, company = product
  print(company)