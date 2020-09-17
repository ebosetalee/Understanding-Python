albums = [
    ("Welcome to my Nightmare", "Alice Cooper", 1975,
     [
         (1, "Welcome to my Nightmare"),
         (2, "Devil's Food"),
         (3, "The Black Widow"),
         (4, "Some Folks"),
         (5, "Only Women Bleed"),
     ]
     ),
    ("Bad Company", "Bad Company", 1974,
     [
         (1, "Can't Get Enough"),
         (2, "Rock Steady"),
         (3, "Ready for Love"),
         (4, "Don't Let Me Down"),
         (5, "Bad Company"),
         (6, "The Way I Choose"),
         (7, "Movin' On"),
         (8, "Seagull"),
     ]
     ),
    ("Nightflight", "Budgie", 1981,
     [
         (1, "I Turned to Stone"),
         (2, "Keeping a Rendezvous"),
         (3, "Reaper of the Glory"),
         (4, "She Used Me Up"),
     ]
     ),
    ("More Mayhem", "Imelda May", 2011,
     [
         (1, "Pulling the Rug"),
         (2, "Psycho"),
         (3, "Mayhem"),
         (4, "Kentish Town Waltz"),
     ]
     ),
]
# This is a list, containing tuples containing a list which contains tuples.
# i.e a list of tuples having a list of tuples.

for name, artist, year, songs in albums:
    print("\nAlbum: {0}, Artist: {1}, Year: {2}, Songs: {3}"
        .format(name, artist, year, songs))

print() # for spacing
# to pick each album by index:
album = albums[2]
print(album)
# this is the budgie album.

print()
# You can index through the album:
songs = album[3]
print(songs)

print()
# You can index through the songs, It will print a tuple:
song = songs[1]
print(song)

print()
# To get just the title from the song tuple, It's all about indexing:
print(song[1])

print()
# To get the mayham song in one code:
mayhem = albums[3][3][2][1]
# This is the same as the code from lines 49-65
print(mayhem)

# In simple terms:
print(albums[3])
print(albums[3][3])
print(albums[3][3][2])
print(albums[3][3][2][1])

# note: this is the same as:
for index, (title, artist, year, songs) in enumerate(albums):
    print("{}: {}, {}, {}, {}."
    .format(index, title, artist, year, songs))

print()

for index, value in enumerate(albums):
    title, artist, year, songs = value
    print(index, title, artist, year, songs)