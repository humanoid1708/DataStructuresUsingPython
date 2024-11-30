#LinearSearchMethod
def FindCloseLS(arr, target):
    diff = float("inf")
    closest = 0
    for i in range(len(arr)):
        if abs((arr[i] - target)) < diff:
            diff = abs((arr[i] - target))
            closest  = arr[i]
    return closest

#BinarySearchMethod
def FindCloseBS(arr, target):
    minDiff = minDiffLeft = minDiffRight = float("inf")
    close = None
    low = 0
    high = len(arr) - 1
    while low < high:
        mid = (low + high) // 2
        if mid + 1 < len(arr):
            minDiffRight = abs(arr[mid + 1] - target)

        if mid > 0:
            minDiffLeft = abs(arr[mid - 1] - target)

        if minDiffLeft < minDiff:
            minDiff = minDiffLeft
            close = arr[mid-1]

        if minDiffRight < minDiff:
            minDiff = minDiffRight
            close = arr[mid+1]

        if arr[mid] < target:
            low = mid + 1

        elif arr[mid] > target:
            high = mid - 1
            if high < 0:
                return arr[mid]
        else:
            return arr[mid]
            
        return close
    
arr = [1,2,5,9]
print(FindCloseBS(arr, -7))