# The enumerate function returns each item, with its index position.

# for number, part in enumerate(available_parts):
#    print("{0}: {1}".format(number + 1, part))

for index, character in enumerate("abcdefgh"):
    print(index, character)

# its built into python to provide an efficient way to get indexes, as well as values in a loop.