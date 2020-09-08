# iterators go through a string one after the other
#  it goes through the data in a string one element at a time
#  strings and lists are examples of iterators

# Create a list of items (you may use either strings or numbers in the list),
# then create an iterator using the iter() function.
# 
# Use a for loop "n" times, where n is the number of items in your list.
# Each time round the loop, use next() on your list to print the next item.
# 
# hint: use the len() function rather than counting the number of items in the list.

ansan = ["1", "i am sorry", "2", "i'm not insecure", "3", "he's just too close to her", "4", "he'll probably never notice it", "5", "don't fuck up"]

ans = [1,2,3,4,5,6,7,8,9]
for char in iter(ans):
  if char == len(ans):
    print((char))
my_iterator = iter(ansan)

for i in range(0, len(ansan)):
  next_item = next(my_iterator)
  print(next_item)

for i in ansan:
  print(i)