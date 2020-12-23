# Creating a Sets.
# Normal Set Declaration
farm_animals = {"Cow", "Sheep", "Buffalo"}
print(farm_animals)
for animals in farm_animals:
    print(animals)
print("*" * 80)
# Set Constructor Method to Declare Sets
wild_animals = set(["lion", "tiger", "panther", "Deer"])  # We can pass there tuple, tuple and range
print(wild_animals)
for animals2 in wild_animals:
    print(animals2)
print()
# Creating Empty Set
empty_set= set()
empty_set.add("Horse")
# empty_set2 = {}
# empty_set2.add("Horse")  # This line will cause an error cause when we declared our emptry_set2 it became dict.
# So there is only one way to declare a empty set and that is set constructor method

# Passing tuple and list and range in set constructor method
demo1 = set(("hare","here","hire"))
demo2 = set(("hare","here","hire"))
demo3 = set(range(2,20,8))
print(demo1,demo2,demo3)