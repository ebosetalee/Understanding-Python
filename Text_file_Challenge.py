# Write a program to append the times table to our jabberwocky poem in sample.txt. We want the tables from 2 to 12 (similar to the 
# output) from the For loops part 2 lecture in setion 6).
#
# The first column of numbers should be right justified. As an example, the 2 times tabe should look like this:
#   1 times 2 is 2
#   2 times 2 is 4
#   3 times 2 is 6
#   4 times 2 is 8
#   5 times 2 is 10
#   6 times 2 is 12
#   7 times 2 is 14
#   8 times 2 is 16
#   9 times 2 is 18
#  10 times 2 is 20
#  11 times 2 is 22
#  12 times 2 is 24
#  ----------------
#    SOLUTION:
# first create a different file of samples.txt, to not change the sample.txt file.

with open ("samples.txt", "a+") as text_file:
    text_file.seek(0)
    text_file.write("\n")
    for length in range(2,13):
            for multiply in range(2,13):
                print("{1:>2} times {0} is {2}".format(length, multiply, length*multiply), file=text_file)
            print("-" * 40, file=text_file)