from jukebox_data import albums
from colour_type import *


SONG_LIST_INDEX = 3
SONG_TITLE_INDEX = 1
# to understand, read constant in Array, List, Tuples/constant.txt

while True:
    print(GREEN,"\nPlease choose your album (invalid choice exits): ")
    for index, (title, artist, year, songs) in enumerate(albums):
        print("{0}: {1}.".format(index + 1, title))

    try:
        choice = int(input( ))
        if 1 <= choice <= len(albums):
            songs_list = albums[choice -1][SONG_LIST_INDEX]
        else:
            break
    except:
        print(RED, "Must be a track number. Try again")
        continue

    print("\nPlease choose your song: ", BLUE)
    for index, (track_number, song) in enumerate(songs_list):
        print("{0}: {1}.".format(index + 1, song), MAGENTA)

    song_choice = int(input( ))
    if 1 <= song_choice <= len(songs_list):
        title = songs_list[song_choice -1][SONG_TITLE_INDEX]
        print("\nPlaying {}!".format(title))
        print("=" * 40)  

    print()
