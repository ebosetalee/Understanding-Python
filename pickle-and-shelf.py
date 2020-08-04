# Pickle
# Serialization is the process that allowsbjects to be saved to a file - Java.
# The mechanism for serializing objects is called PICKLING(pickel).
# When an object is pickled and its written to a file in a format atht contains 
# the objects data together with sufficient information
# to allow that object to be recreated when its loaded back in. We've seen converting
# an object to byte array inorder to save it into a binary file isn't so easy, and no 
# information about the object itself is stored unless we write code to do that.
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

# with open("imelda.pickle", "rb") as imelda_pickle:
#     imelda2 = pickle.load(imelda_pickle)
    
# print(imelda2)

# album, artist, year, tracklist = imelda2
# print(album)
# print(artist)
# print(year)
# for track in tracklist:
#     track_number, track_title = track
#     print(track_number, track_title)
# 
# # we can pickle as many objects as we want in the file
imelda = ("More Mayhem", 
    "Imelda May", 
    2011, 
    ((1, "Pulling the Rug"), 
    (2, "Psycho"), 
    (3, "Mayhem"), 
    (4, "Kentish Town Waltz"))) 

even = list(range(0, 10, 2))
odd = list(range(1,10, 2))

with open("imeldas.pickle", "wb") as pickled_file:
    pickle.dump(imelda,pickled_file)
    pickle.dump(even,pickled_file)
    pickle.dump(odd,pickled_file)
    pickle.dump(2998302,pickled_file)

with open("imeldas.pickle", "rb") as imelda_pickled:
    imelda2 = pickle.load(imelda_pickled)
    even_list = pickle.load(imelda_pickled)
    odd_list = pickle.load(imelda_pickled)
    x = pickle.load(imelda_pickled)
# to load all the items dumped in it

print(imelda2)

album, artist, year, tracklist = imelda2
print(album)
print(artist)
print(year)
for track in tracklist:
    track_number, track_title = track
    print(track_number, track_title)

print("="*40)
for i in even_list:
    print(i)

print("="*40)
for i in odd_list:
    print(i)

print("="*40)
print(x)

# NOtE: the objects must be reasd back in the same order they were written
# There are only a few items in python that can't be saved by pickling them
# Also, pickling is better than converting them to binaries
# There are issues of versions from python 3.4 are unpackle i.e aren't
# backwards compatible. In order words, the version 4 from earlier python versions
# the protocols aren't backwards compatible.
# 
# The original pickle protocol was human readable. Thus, we can change the way we
# save the data by specifying the protocol and then look at the file itself that 
# is produced. It can be seen as follows: 

with open("imeldas2.pickle", "wb") as pickled_files:
    pickle.dump(imelda,pickled_files, protocol=0)
    pickle.dump(even,pickled_files, protocol=0)
    pickle.dump(odd,pickled_files, protocol=0)
    pickle.dump(2998302,pickled_files, protocol=0)

with open("imeldas2.pickle", "rb") as imelda_pickles:
    imelda23= pickle.load(imelda_pickles)
    even_list1 = pickle.load(imelda_pickles)
    odd_list1 = pickle.load(imelda_pickles)
    x1 = pickle.load(imelda_pickles)

print(imelda23)

album, artist, year, tracklist = imelda23
print(album)
print(artist)
print(year)
for track in tracklist:
    track_number, track_title = track
    print(track_number, track_title)

print("="*40)
for i in even_list1:
    print(i)

print("="*40)
for i in odd_list1:
    print(i)

print("="*40)
print(x1)
# it is easy to read but doesn't make complete sense but the numbers in the data are
# delimited with a capital I. That's the point there. This is for protocol=0.

# There's protocol=1 i.e protocol version 1 which is the first binary protocol in
# old versions of python should be able to unpick the data created with that protocol.

# Python 2.3 introduced the protocol version 2 which could pick up classes more efficiently
# The version has a number security checks removed that was declared insecure and for that
# reason, It's better not to use it.
# 
# The first python 3 version came with protocol 3 which is also the default protocol which
# is used if you don't specify one. Just like above. However, data created won't be 
# readable in python 2.7 or any version of python 2. 
# 
# The protocol used to pickle objects can be determined by python automatically. Thus, 
# no need to specify a protocol. Also you can use different protocols in the same file as 
# seen above OR   
with open("imeldas3.pickle", "wb") as pickleS_files:
    pickle.dump(imelda,pickleS_files, protocol=pickle.HIGHEST_PROTOCOL)
    pickle.dump(even,pickleS_files, protocol=0)
    pickle.dump(odd,pickleS_files, protocol=pickle.DEFAULT_PROTOCOL)
    pickle.dump(2998302,pickleS_files, protocol=1)
    # This will still work

with open("imeldas3.pickle", "rb") as imeldas_pickles:
    imelda3= pickle.load(imeldas_pickles)
    even_list2 = pickle.load(imeldas_pickles)
    odd_list2 = pickle.load(imeldas_pickles)
    x2 = pickle.load(imeldas_pickles)

print(imelda3)

album, artist, year, tracklist = imelda3
print(album)
print(artist)
print(year)
for track in tracklist:
    track_number, track_title = track
    print(track_number, track_title)

print("="*40)
for i in even_list2:
    print(i)

print("="*40)
for i in odd_list2:
    print(i)

print("="*40)
print(x2)
# Everything still prints the same. The difference is in the file created 
# and how they are read or seen immediately.
# The security in data saved with pickle is unsure. Thus, you should
# only unpickle data you can trust.
# Pickling is fun for storing your program's data but shouldn't be used 
# when dealing with data from untrusted sources such as over the internet
# for argument's sake. It is very easy to wreck havoc by unpickling data
# that can't be trusted as seen below.
# 
# NOte: rm is to remove file from mac/linux
# Check this link for more details https://docs.python.org/3/library/pickle.html 


# Pickle has a draw back i.e the objects all have to be loaded back into memory
# i.e the computer's memory that's fine for some situations but dealing with large 
# set of objects e.g a large dictionary then loadng that to memory may not be a
# realistic option. Thus, the alternative is to use the Shelve Module.  