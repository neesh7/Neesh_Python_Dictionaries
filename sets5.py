# There are Two Sets
A = {1, 2, 3, 4, 5, 6, 8, 11, 22, 23}
B = {5, 6,}
C = set(range(0,40,2))

if B.issubset(A):
    print("B is subset of A  ")
if C.issuperset(A):
    print("C is superset of A")
