import shelve

# blt = ["bacon", "lettuce", "tomato", "bread"]
# beans_on_toast = ["beans", "bread"]
# scrambled_eggs = ["eggs", "butter", "milk"]
soup = ["tin of soup"]
# pasta = ["pasta", "cheese"]

with shelve.open("recipes", writeback=True) as recipes:
    # recipes["blt"] = blt
    # recipes["beans_on_toast"] = beans_on_toast
    # recipes["scrambled_eggs"] = scrambled_eggs
    # recipes["pasta"] = pasta
    # don't forget the quotes for string. Shelf must be string.
    # recipes["soup"] = soup

    # for snack in recipes:
    #     print(snack, recipes[snack])

# how to modify an item in it:
# if we do this, our items aren't updated:
    recipes["blt"].append("butter")
    recipes["pasta"].append("tomato")

    print("--" * 40)

# The issue is the shelf has no way to know that the lists have changed because 
# what we've done is to append the items to a copy of the list read into memory 
# but we haven't provided any trigger for the shelve to write data back out again.
# This is so to keep the disk access to an absolute minimum. 
# Thus, we can try it in two ways:
# 1. we do create a list from the recipes shelve append to the list and write it to the shelve:
    # temp_list = recipes["blt"]
    # temp_list.append("butter")
    # recipes["blt"] = temp_list

    # temp_list = recipes["pasta"]
    # temp_list.append("tomato")
    # recipes["pasta"] = temp_list

    # for snack in recipes:
    #     print(snack, recipes[snack])
# 2. opening the shelve with writeback set to true. In this, we change the withstatement adding writeback 
# e.g with shelve.open("recipes", writeback=True) as recipes:, then append
    recipes["soup"].append("croutons")

    for snack in recipes:
        print(snack, recipes[snack])

# instead of writing the long line of code, the writeback method updates the list but doesn't actually 
# update the shelve until you close the shelve or use the sync method.

# There's a potential problem with using that sync method causes all entries in the cache to be written to 
# disk but it also clears the cache as well so sync is called automatically when the shelve is closed but 
# you can also use it anywhere anytime you want to force the data files to be updated:
    # recipes.sync()

# When is it appropriate to use shelve:
# Shelve only accepts strings, can be used in the same way as dictionaries.
# Note, in shelve, the values are pickled before being stored in the underlying database fields.
# However, it is not suitable for some applications where the values ae complex because of pickling and unpickling may affect the performance.
# Also concurrent access can also be a problem with shelves although concurrent read accesses are safe 
# if a program is writing to the shelve and no other programs should have it open or attempt to open it.
# Thus, it may be preferable to store data in a database rather than using shelves
