import bisect

A = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
print("bisect.left returns first occurrance index")
print(bisect.bisect_left(A, 108))
print(bisect.bisect_left(A, 285))
print(bisect.bisect_left(A, -10))

print("bisect.right returns index after rightmost occurrance")
print(bisect.bisect_right(A, 108))
print(bisect.bisect_right(A, 285))
print(bisect.bisect_right(A, -10))

print("same as bisect.right is bisect")
print(bisect.bisect(A, 108))
print(bisect.bisect(A, 285))
print(bisect.bisect(A, -10))

bisect.insort_left(A, 109)
print(A)
bisect.insort_right(A, 10)
print(A)
