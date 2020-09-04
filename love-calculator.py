import random
name1 = random.choice(["timi", "funmi", "jasmine", "praise", "anna", "lisa" ])
name2 = random.choice(["seun", "joseph", "frank", "daniel", "bayo", "david"])

calculator_name = name1 + "loves" + name2
print(calculator_name)

love_algorithm = ""

index = 0
while index < len(calculator_name):
    count = 0
    letter = calculator_name[index]
    for x in calculator_name:
        if x == letter:
            count += 1
    index += 1
    love_algorithm += str(count)
print(love_algorithm)


while len(love_algorithm) > 2:
    new_love_algorithm = ""
    index1 = 0
    index2 = len(love_algorithm) - 1
    fixed_length = len(love_algorithm) / 2
    while index1 < fixed_length:
        if index1 != index2:
            val = int(love_algorithm[index1]) + int(love_algorithm[index2])
            new_love_algorithm += str(val)
        else:
            val = int(love_algorithm[index1])
            new_love_algorithm += str(val)
        index1 += 1
        index2 -= 1
    love_algorithm = new_love_algorithm
    print(new_love_algorithm)
    if len(love_algorithm) == 2:
        print("The love percentage is {}%".format(new_love_algorithm))
