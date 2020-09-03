# One more thing to look at a common source of errors when you're converting a dictionary that is initialized using a literal into a shelve:
# using the recipes we'll make the dictionary a bit complicated by adding dictionary books.
import shelve


# books = {"recipes": {"blt":["bacon", "lettuce", "tomato", "bread"],
#                      "beans on toast": ["beans", "bread"],
#                      "scrambled eggs": ["eggs", "butter", "milk"],
#                      "soup": ["tin of soup"],
#                      "pasta": ["pasta", "cheese"]},
#          "maintenance": {"stuck": ["oil"],
#                          "loose": ["gaffer tape"]}}

# print(books["recipes"]["soup"])
# print(books["recipes"]["scrambled eggs"])

# print(books["maintenance"]["loose"])


books = shelve.open("book")
books["recipes"] = {"blt":["bacon", "lettuce", "tomato", "bread"],
                    "beans on toast": ["beans", "bread"],
                    "scrambled eggs": ["eggs", "butter", "milk"],
                    "soup": ["tin of soup"],
                    "pasta": ["pasta", "cheese"]}
books["maintenance"] = {"stuck": ["oil"],
                        "loose": ["gaffer tape"]}

print(books["recipes"]["soup"])
print(books["recipes"]["scrambled eggs"])

print(books["maintenance"]["loose"])
# This looks good but when we run it we get an error :
# print(books["recipes"]["soup"])
# TypeError: tuple indices must be integers or slices, not str.
# The problem is the comma left in line 25 = "pasta": ["pasta", "cheese"]},
books.close()