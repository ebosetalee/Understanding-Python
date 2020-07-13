# open the file, read in the file, close the file.
# using sample.txt
# jabber = open("sample.txt", "r")

# for line in jabber:
#     if "jabberwock" in line.lower():
#         print(line, end=" ")

# jabber.close()

# THIS CAN BE WRITTEN IN ANOTHER WAY AS SEEN BELOW:

# with open("sample.txt", "r") as jabber:
#     for line in jabber:
#         if "JAB" in line.upper():
#             print(line, end="") # using the with statement the file closes at the end.


# We could use readline which reads a single line from a file and returns a string, As seen below:
# with open("sample.txt", "r") as jabber:
#     line = jabber.readline()
#     while line:
#         print(line, end=" ")
#         line = jabber.readline()
# Another is Readlines which reads the entire file at once and returns a list of strings, it isn't convenient for a large file

with open("sample.txt", "r") as jabber:
    lines = jabber.readlines()
print(lines) # This is useful for debugging purposes; to understand the data.

for line in lines:
    print(line, end="")

# Another is read which reads the entire file and if it's a text, returns a string contaning the contents of the file.
with open=n("sample.txt", "r") as jabber:
    lines = jabber.read()

for line in lines[::-1]:
    print(line, end="")
# read can take an optional parameter specifying how much data to read.