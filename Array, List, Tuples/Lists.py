even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

print(min(even))
print(max(even))
print(min(odd))
print(max(odd))

numbers = odd + even
# numbers.sort()
# is command is used to check if the two are identically equal 
# == checks if the content is both are equal
numers_in_order = sorted(numbers)
print(numers_in_order)
# numero = set(numbers)
print(set(numbers))
# another_even = sort(numbers, reverse = True) this doesnt work
another_even = sorted(numbers, reverse=True)
# ans = sorted(numbers, reverse=True) this works
print(another_even)
# print(ans)
print(numbers)
print(another_even == numers_in_order)
print(another_even is numers_in_order)
numers = [even, odd]
print(numers)
for number_set in numers:
  print(number_set)
  for value in number_set:
    print(value)

print()
print("mississippi".count("s"))