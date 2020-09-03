# using For loop to create timestable and creating a new file.

for length in range(1,12):
    for multiply in range(1,12):
            print(" {1} times {0} is {2}".format(length, multiply, length*multiply))
    print("\n")

with open ("sample2.txt", "w") as text_file:
    text_file.write("\n")
    for length in range(2,13):
            for multiply in range(2,13):
                print("{1:>2} times {0} is {2}".format(length, multiply, length*multiply), file=text_file)
            print("-" * 40, file=text_file)