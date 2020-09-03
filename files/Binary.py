# Binary is a base 2 number system, otherwise known as binary number system.
# What is a binary? Binary only uses the digits 0 - 1.
for i in range(17):
   print("{0:>2} in binary is {0:>08b}".format(i))
# this shows the decimal equivalent of the field with the 2, then right aligning
# to the value of i, then we're specifying a of 8.
# the binary right align and adding beta with the value of i in binary. 
# in other words, it means {0:>2} the first zero is the index parametervin the format argument.
# The > is saying the number should be right aligned and the 2 is saying it should be by 2 digits. 
# The b means binary and the 08b means binary number with 8 digits. 

# Subraction works the same as it does in decimal.
# OR and AND 
# XOR - exclusiveOR Sets the corresponding bit of the result to one if either but not both 

# NOTE converting from decimal to binary is tedious once you get up above four bits (digits)or eight numbers
#   