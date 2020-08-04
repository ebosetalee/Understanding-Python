import shelve

# with shelve.open("bike") as bike:
#     bike["make"] = "Honda"
#     bike["model"] = "250 dream"
#     bike["colour"] = "red"
#     bike["engine_size"] = 250

#     print(bike["engine_size"])
#     print(bike["colour"])

# One aspect of shelve we should bear in mind is that
# Unlike dictionary examples where we can run the program
# again, shelves are persistent files, in the sense that
# if a key is typed with an erroe, that key is saved and
# can be retrieved anytime. e.g
# bike["engin_size"] = 250

# with shelve.open("bike2") as bike:
#     bike["make"] = "Honda"
#     bike["model"] = "250 dream"
#     bike["colour"] = "red"
#     bike["engine_size"] = 250

#     for key in bike:
#         print(key)

#     print("--"* 40)


#     print(bike["engine_size"])
#     print(bike["colour"])

# But like a dictionary, we can use Del to remove items from a shelve.

with shelve.open("bike2") as bike:
    bike["make"] = "Honda"
    bike["model"] = "250 dream"
    bike["colour"] = "red"
    bike["engine_size"] = 250

    del bike["engin_size"]

    for key in bike:
        print(key)

    print("--"* 40)


    print(bike["engine_size"])
    print(bike["colour"])

# It no longer exists.
