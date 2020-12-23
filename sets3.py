# There are Two Sets
A = {1, 2, 3, 4, 5, 6}
B = {5, 6, 7, 8, 9, 10}
print("SET A:", A, ",", "SET B:", B)
print("Union of A and B :", A.union(B))
print("Intersection of A and B:", A.intersection(B))
print("Intersection of A and B:", A & B)
print("In Order to Print only A or only B we Need to Find Difference of Sets using any of two methods:")
print("Only A:", sorted(A.difference(B)))
print("Only B:", sorted(B.difference(A)))
# print(A.difference_update(B))
# A.difference_update(B)
print("A:{}".format(A), "\nB:{}".format(B))
print("Symmetric difference is union of only A and only B")
print(A.symmetric_difference(B))