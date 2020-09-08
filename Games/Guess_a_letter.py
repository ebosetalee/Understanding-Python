import random
my_list = ["I", "eat", "chicken", "and", "turkey"]
random_word = str(random.choice(my_list))
print(random_word.upper())

new_list = ""
for letters in my_list:
    new_list += letters 
# print(new_list)

word = input("Kindly type one letter only: ")
index = 0
while index < len(new_list):
    if word in new_list[index]:
        print("YES in {}".format(index))
    index += 1
if word not in new_list:
    print("NO")