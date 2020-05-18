# This is described as the combination in single statement of a binary
# operation and an assignment statement. 
# cancatenation is a binary operation
# highly disappointed but augmented assignment is simply using += or -= or /= or *=
# or **= 
# binary operators include: +=, -=, *=, /=, !=, %=, **=, <<=, >>=, &=, ^=, |=.
#   | means Union, & means intersection, ^ means symmetrical difference.
number = 5
multiplier = 8
answer = 0

# add your loop after this comment
for i in range(multiplier):
    answer += number

print(answer) 

stain = 0
for x in range(0,8):
    #stain += 5
    print(x)


ipAddress = input("Please enter an IP Adress: ")

# Our starting point is at least one segment, that has length 0
segment = 1
segment_length = 0
character = ""
 
# Loop through the supplied IP Address
for character in ipAddress:
    if character == '.':
        # The current character IS '.', so print out the details for this segment
        print("segment {} contains {} characters".format(segment, segment_length))
        # And now start a new segment with length 0
        segment += 1
        segment_length = 0
    else:
        # The current character IS NOT '.', so we stay in the this segment, but add 1 to the length
        segment_length += 1
# Unless the final character in the string was a . then we haven't printed
# the last segment
if character != '.':
    print("segment {} contains {} characters".format(segment, segment_length))
