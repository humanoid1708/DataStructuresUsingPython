def Peak(arr):
    if len(arr) < 3:
        return None
    low = 0
    high = len(arr)-1


    while low <= high:
        mid =  (low + high) // 2
        midLeft = arr[mid-1] if mid - 1 > 0 else float("-inf")
        midRight = arr[mid+1] if mid + 1 < len(arr) else float("inf")
        
        if midLeft < arr[mid] and arr[mid] < midRight:
            low = mid+1

        elif midRight < arr[mid] and arr[mid] < midLeft:
            high = mid-1

        elif midLeft < arr[mid] and midRight < arr[mid]:
            return arr[mid]
    return None

arr = [1,2,5,4,3,2,1]
A1 = [1, 2, 3, 4, 5]
A2 = [5, 4, 3, 2, 1]
print(Peak(arr))
print(Peak(A1))
print(Peak(A2))