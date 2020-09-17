# This helps in switching dictionary to a shelve and vice versa.
# CHALLENGE:
# Modify the program from the dictionary challenge to use shelves instead of dictionaries
# 
# Do this by creating two programs, cave_initialise.py should create the two shelves 
# (location and vocabulary) with the appropriate keys and values.
# 
# cave_game.py will then use the two shelves instead of dictionaries.
# Apaert from opening and closing the shelves, cave_game will need only
# two changes to the actual code - remember that shelf keys MUST be string!
# 
# Just to be clear, cave_game.py will contain the code for the game, everything
# before that (modified to use shelves) will be in cave_initialise.py 


locations = {
  0: {"desc": "You are sitting in front of a computer learning Python",
      "exits": {},
      "namedExits":{}},
  1: {"desc": "You are standing at the end of a ROAD before a small brick building",
      "exits": {"W": 2, "E" : 3, "N" : 5, "S" : 4, "Q" : 0},
      "namedExits": {"2": 2, "3": 3, "5": 5, "4": 4}},
  2: {"desc": "You are at the top of a HILL",
      "exits": {"N": 5, "Q" : 0},
      "namedExits": {"5": 5}},
  3: {"desc": "You are inside a BUILDING, a well house for a small stream",
      "exits": {"W": 1, "Q" : 0},
      "namedExits": {"1": 1}},
  4: {"desc": "You are in a VALLEY beside a stream",
      "exits": {"N": 1, "W" : 2, "Q" : 0},
      "namedExits": {"1": 1, "2": 2}},
  5: {"desc": "You are in a FOREST",
      "exits": {"W": 2, "S" : 1, "Q" : 0},
      "namedExits": {"2": 2, "1": 1}}
}
vocabulary = {
    "QUIT": "Q",
    "NORTH": "N",
    "SOUTH": "S",
    "EAST": "E",
    "WEST": "W",
    "ROAD": "1",
    "HILL": "2",
    "BUILDING": "3",
    "VALLEY": "4",
    "FOREST": "5"} 
