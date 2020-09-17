import cave_initialise as start


loc = "1"
while True:
  availableExits = ", ".join(start.locations[loc]["exits"].keys())
  print(start.locations[loc]["desc"])

  if loc == "0":
    break 
  else:
    allExits = start.locations[loc]["exits"].copy()
    allExits.update(start.locations[loc]["namedExits"])

  direction = input("Available exits are "+ availableExits + " choose one only please  ").upper() 
  print()
  if len(direction) > 1: 
    words = direction.split()
    for word in words:
      if word in start.vocabulary:
        direction = start.vocabulary[word]

  if direction in allExits: 
    loc = allExits[direction] 
  else:
    print("You cannot go in that direction")

start.locations.close()
start.vocabulary.close()