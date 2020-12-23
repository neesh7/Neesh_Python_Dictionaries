locations = {0: "You are sitting in front of a computer learning Python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}

exits = {0: {"Q": 0},
         1: {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},  # road
         2: {"N": 5, "Q": 0},  # Hill
         3: {"W": 1, "Q": 0},  # BUilding
         4: {"N": 1, "W": 2, "Q": 0},  # Valley
         5: {"W": 2, "S": 1, "Q": 0}}  # Forest

vocab = {"QUIT":  "Q",
         "EAST":  "E",
         "WEST":  "W",
         "SOUTH": "S",
         "NORTH": "N"
         }
# Explanation : IN the next line it is being writen that loc = 1 .why that is..cz our exits is a list of dictionaries
loc = 1  # We are starting from road that's why its =1
while True:
    availableExits = ", ".join(exits[loc].keys())

    print(locations[loc])

    if loc == 0:
        break

    direction = input(
        "Available exits are " + availableExits + " ").upper()  # Upper converts the input into the upper case
    if len(direction) > 1:
        for word in vocab:
            if word in direction:
                direction = vocab[word]
    print()
    if direction in exits[loc]:
        loc = exits[loc][direction]
    else:
        print("You cannot go in that direction")

