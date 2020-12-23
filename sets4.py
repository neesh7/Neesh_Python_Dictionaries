# Removing items in sets
# we got two ways to do it . "Remove" and another one is "Discard"
# Remove will raise an error if the set doesn't contain that entry but discard will not raise an error in that case
# There are Two Sets
A = {1, 2, 3, 4, 5, 6}
B = {5, 6, 7, 8, 9, 10}
A.remove(6)
B.remove(6)
A.discard(5)
B.discard(5)
print("A:{}, B:{}".format(A,B))
print("We can see that element 5 and 6 is being removed from both sets")
# Undesired removal
# A.remove(11)  # Causes an error as the entry is unavailable in set A
A.discard(11) # Doesn't raise an error even if the entry is unavailable in the set
print(sorted(A))
print()
# Using exception in order to track an error
# user_input = int(input("Enter the Element you want to remove from Set A"))
try:
    A.remove(99)
except KeyError:
    print("This  Element is not a member  of the Set A")