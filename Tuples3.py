welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
bad = "Bad company!" " Bad company!!", 1974
budgie = "Nightlight", "Budgie", 1981
imelda = "More Mayhem", "Emilda May", 2011, (
    (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))

print(imelda)

title, artist, year, tracks = imelda
print(title)
print(artist)
print(year)
print(tracks)
# notice how  tracks has been returned as a tuple in its own right
# when adding extra tuples, it is important to enclose the four individual songs
# the track number and actual song in parenthesis otherwise the python interpreter
# will evaluate that as a single tuple with eight elements

# It is possible to extract the individual tracks as seen below :
# by changing track to track 1, track 2, track3 and track4
# and getting rid of the initial bracket;

imelda = "More Mayhem", "Emilda May", 2011, (1, "Pulling the Rug"), (
    2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz")

title, artist, year, track1, track2, track3, track4 = imelda
print(title)
print(artist)
print(year)
print(track1)
print(track2)
print(track3)
print(track4)
# the problem of this method is we need to know how many tracks available
# and set or create variables for each.

imelda = "More Mayhem", "Emilda May", 2011, 1, "Pulling the Rug", 2, "Psycho", 3, "Mayhem", 4, "Kentish Town Waltz"

# unpacking tuples and list:
albums = [("Welcome to my Nightmare", "Alice Cooper", 1975),
          ("Bad company!", " Bad company!!", 1974),
          ("Nightlight", "Budgie", 1981),
          ("More Mayhem", "Emilda May", 2011),
          ("Ride the lightening", "Metallica", 1984)]

for name, artist, year in albums:
    print("\nAlbum: {0}, Artist: {1}, Year: {2}"
        .format(name, artist, year))
    
# OR

for album in albums:
    name, artist, year = album
    print("\nAlbum: {0}, Artist: {1}, Year: {2}"
        .format(name, artist, year))
