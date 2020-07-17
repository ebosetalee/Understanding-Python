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
    for y in range(17):
        bin_file.write(bytes([y]))

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

# to_bytes method: the first is for the number of bytes we want, and the second is whetehr to return the result as big indie or little indie
# The number of bytes is straight forward; as seen, the largest number that we can store in two bytes or 16 bits i.e 65535
# If we get a higher number, we need more bytes to store those numbers. In c, we need at least 3 bytes to represent that variable but usually,
# when you're writing binary to use an even number of bytes, that's why we've converted it up to 4 in that case.
# The big is for the computer to make a decision on how to store numbers in memory. What happens is "big" stores the most significant byte 
# first with the remaining bytes of the numberf following in that order; While little indie is the reverse as it shows the least significant
# byte being storedc first.
# The initial choice was arbitrary e.g IBM choosing big indie for their mainframes and Intel, Intel and CPU's used for their manufacturer are using 
# little indie for their early microprocessors.
# Thus, once the choice has been made, it continues to be used and maintained backward compatibility.
# What we'll do is to read the numbers back into our program before we move on to more ways to store number variables to binary file
# 
with open ("binary2", "br") as bins_file: #remember to put .read (to read the file)
    e = int.from_bytes(bins_file.read(2), "big")
    print(e)
    f = int.from_bytes(bins_file.read(2), "big")
    print(f)
    g = int.from_bytes(bins_file.read(4), "big")
    print(g)
    h = int.from_bytes(bins_file.read(4), "big")
    print(h)
    i = int.from_bytes(bins_file.read(4), "big")
    print(i)
    # The difference in the output is because the bytes are in reversed order from little indie to big indie. Thus, understanding the
    # structure of binary data in a file. 