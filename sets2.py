# Operations on Sets
even = set(range(0, 40, 2))
print("Our even set is:",even)
print("length of even set is:",len(even))
squared_tuple = (4, 9, 16, 25, 49)
squares = set(squared_tuple)
print()
print("Squares set is:",squares)
print("Length of squares is:",len(squares))
print("_" * 40)
# Union of Sets
# union of sets means joining two set together and no elements should be repeated
print("Here .union() method is used which will find union of two sets")
print("union:", even.union(squares))
print("Lenght of union of two sets is :",len(even.union(squares)))
# Other way for writing same code is
print(squares.union(even))
print(len(squares.union(even)))
print("_" * 80)
# Intersection of sets

print("Intersection", even.intersection(squares))
print(even & squares)
print("Intersection length", len(even.intersection(squares)))
# other way to write about intersection
print(squares.intersection(even))
print(squares & even)
print(len(squares.intersection(even)))

# Difference of Sets
print("#" * 80)
# it's not neccessary to sort our set but in order to observ the mathematics clearly we do sort them
even = set(range(0, 40, 2))
print(sorted(even))
print(len(even))
squared_tuple = (4, 9, 16, 25, 49)
squares = set(squared_tuple)
print(sorted(squares))
print(len(squares))
# finding difference of sets
print("even minus squares")
print(sorted(even.difference(squares)))
print(sorted(even-squares))
# other way to do this is
print("squares minus even")
print(sorted(squares.difference(even)))
print(sorted(squares-even))
print("Thank You")