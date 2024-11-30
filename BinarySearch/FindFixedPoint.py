#LinearSearchMethod
def FindFixLS(arr):
    for i in range(len(arr)):
        if arr[i] == i:
            return i
    return None

#BinarySearchMethod
def FindFixBS(arr):
    low = 0
    high = len(arr)-1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == mid:
            return mid
        if arr[mid] > mid:
            high = mid - 1
        if arr[mid] < mid:
            low = mid + 1
    return None

arr = [-1, 0, 1, 2, 4]
A1 = [-10, -5, 0, 3, 7]
A2 = [0, 2, 5, 8, 17]
A3 = [-10, -5, 3, 4, 7, 9]
print(FindFixLS(arr))
print(FindFixBS(A1))
print(FindFixBS(A2))
print(FindFixLS(A3))