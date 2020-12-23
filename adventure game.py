locations = {0: "You are sitting in front of a computer learning Python",
             1: "You are standing at the end of a road before a small brick building",
             2: "You are at the top of a hill",
             3: "You are inside a building, a well house for a small stream",
             4: "You are in a valley beside a stream",
             5: "You are in the forest"}

exits = [{"Q": 0},
         {"W": 2, "E": 3, "N": 5, "S": 4, "Q": 0},  # road
         {"N": 5, "Q": 0},  # Hill
         {"W": 1, "Q": 0},  # BUilding
         {"N": 1, "W": 2, "Q": 0},  # Valley
         {"W": 2, "S": 1, "Q": 0}]  # Forest

# Explanation : IN the next line it is being writen that loc = 1 .why that is..cz our exits is a list of dictionaries
# and we are using index position 1 for our all available exits . so it is WESNQ
loc = 1  # We are starting from road that's why its =1
while True:
    availableExits = ", ".join(exits[loc].keys())
    # Here join method is used to join all our available keys as a single string so that we could compare our input entries

    print(locations[loc])  # [loc=1]this prints index 1 entries for location

    if loc == 0:
        break

    direction = input("Available exits are " + availableExits + " ").upper()# Upper converts the input in the upper case
    print()
    if direction in exits[loc]: # if the provided input is in the exits[loc=1] so it will update the value of loc
        loc = exits[loc][direction] # here value of loc is being updated using nested indexing technique
        #here loc[loc=1][direction = whatever input is being provided] we can use the key and direction to retrieve the next location.
        # so there is another doubt arises that may be indexing used in a dict can cause a problem cz it is unordered
        # but remember that it is'nt a issue cz it's nested inside a list so it is ordered
    else:
        print("You cannot go in that direction")
