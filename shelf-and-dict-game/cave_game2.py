import shelve


locations = shelve.open("locations")
vocabulary = shelve.open("vocabulary")

loc = "1"
while True:
  availableExits = ", ".join(locations[loc]["exits"].keys())
  print(locations[loc]["desc"])

  if loc == "0":
    break 
  else:
    allExits = locations[loc]["exits"].copy()
    allExits.update(locations[loc]["namedExits"])

  direction = input("Available exits are "+ availableExits + " choose one only please  ").upper() 
  print()
  if len(direction) > 1: 
    words = direction.split()
    for word in words:
      if word in vocabulary:
        direction = vocabulary[word]

  if direction in allExits: 
    loc = allExits[direction] 
  else:
    print("You cannot go in that direction")

locations.close()
vocabulary.close()
# This is another way to solve the challenge.