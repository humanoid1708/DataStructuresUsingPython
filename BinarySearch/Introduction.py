def LinearSearch(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return True
    return False

#Assumes that the arrray is already sorted in ascending order
#Time Complexity is O(logn)
def BinarySearchIter(arr, target):
    low = 0
    high = len(arr) -1
    while low<=high:
        mid = (low+high) // 2
        if target == arr[mid]:
            return True
        elif target < arr[mid]:
            high = mid - 1
        elif target > arr[mid]:
            low = mid + 1
    return False

def BinarySearchRecur(arr, target, low, high):
    if low > high:
        return False
    else:
        mid = (low+high) // 2
        if target == arr[mid]:
            return True
        elif target > arr[mid]:
            return BinarySearchRecur(arr, target, mid+1, high)
        elif target < arr[mid]:
            return BinarySearchRecur(arr, target, low, mid-1)
        
arr = [1,3,5,7,9]
print(LinearSearch(arr, 5))
print(LinearSearch(arr, 4))
print(BinarySearchIter(arr, 1))
print(BinarySearchIter(arr, 8))
print(BinarySearchRecur(arr, 1, 0, len(arr)-1))
print(BinarySearchRecur(arr, 8, 0, len(arr) - 1))


    
