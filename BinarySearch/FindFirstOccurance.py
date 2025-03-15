def Find(arr, target):
    low = 0
    high = len(arr)
    while low <= high:
        mid = (low+high) // 2
        if arr[mid] > target:
            high = mid -1

        elif arr[mid] < target:
            low = mid +1

        else:
            if mid - 1 < 0:
                return mid
            if arr[mid -1] != target:
                return mid
            high = mid - 1

A = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
target = -1
print(Find(A, target))