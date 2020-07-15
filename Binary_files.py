# READING AND WRITING BINARY FILES IN PYTHON.
# This is done because 
# a.) for an image file i.e processing data
# b.)
# The basic principles of reading and writing text files can be applied here.
# Creating a binary file, we specify the mode as b for binary. 
# Note: strings and integers cannot be directly written to a binary file, they need to be converted to a format
# called Bytes. This can be done is several ways but the common method is the BYTES BUILD-IN FUNCTION and then the two underscore
# Bytes method integer objects.

# Lets start by writing the number 0 - 16 (int) to a binary file and then reading them back in.  

with open("binary", "bw") as bin_file:
    for i in range(17):
        bin_file.write(bytes([i]))

with open("binary", "br") as binFile:
    for b in binFile:
        print(b)
# in line 15, we passed a list to bytes function. The reason we passed a list and not just i, is because bite works strangely. In the
# sense that if you pass an integer to bytes it creates a bite sequence with that many bites all set to zero.
# If we have to pass a sequence type i.e a list to the bytes method, then why do we bother iterating through it to create a sngle item
# for each value. The answer is we shouldn't have done that. What we really wanted to do was demonstrate what was happening.

# In practice, this is the right way (Instead of a for loop):
# bin_file.write(bytes(range(17)))


# How to write numerical values greater than 255 to binary file.

# In this example, we write the value out of four variables and allows to read those values back again
# 
#  
a = 65534 # equivalent to FF FE
x = 65535 # equivalent to FF FF
c = 65536 # equivalent to 00010000
d = 29998302 # # equivalent to 002DC01E

with open("binary2", "bw") as bin_files:
    bin_files.write(a.to_bytes(2, "big"))
    bin_files.write(x.to_bytes(2, "big"))
    bin_files.write(c.to_bytes(4, "big"))
    bin_files.write(d.to_bytes(4, "big"))
    bin_files.write(d.to_bytes(4, "little"))