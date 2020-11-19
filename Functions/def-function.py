def calculate_age(before, after):
  diff_age = after - before 
  print(diff_age)
 
calculate_age(10,20)

# Another example:

def calc_age(then, now):
  return now - then

print(calc_age(10,20))

# Simple


def group_by_owners(files):
    new_file = {}
    for index, item in enumerate(files):
        val = item.values
        if val in new_file:
            new_file[val].append(item)
        else:
            new_file[val] = [item]
    return new_file