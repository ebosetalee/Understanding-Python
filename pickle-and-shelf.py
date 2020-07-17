# Pickle
# Serialization is the process that allowsbjects to be saved to a file - Java.
# The mechanism for serializing objects is called PICKLING(pickel).
# When an object is pickled and its written to a file in a format atht contains the objects data together with sufficient information
# to allow that object to be recreated when its loaded back in. We've seen converting an object to byte array inorder to save it into
# a binary file isn't so easy, and no information about the object itself is stored unless we write code to do that.
# Using pickle, savingobjects is very easy as seen below:
import pickle

# imelda = ("More Mayhem", 
#     "Imelda May", 
#     2011, 
#     ((1, "Pulling the Rug"), 
#     (2, "Psycho"), 
#     (3, "Mayhem"), 
#     (4, "Kentish Town Waltz"))) 

# with open("imelda.pickle", "wb") as pickle_file:
#     pickle.dump(imelda,pickle_file)
    # we can read this easily, by using the pickle.load method.

with open("imelda.pickle", "rb") as imelda_pickle:
    imelda2 = pickle.load(imelda_pickle)
    
print(imelda2)

album, artist, year, tracklist = imelda2
print(album)
print(artist)
print(year)
for track in tracklist:
    track_number, track_title = track
    print(track_number, track_title)