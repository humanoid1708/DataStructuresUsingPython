def SQR(target):
    sq = target**(1/2)
    return int(sq)
    
print(SQR(1000))

def SQRUsingBinarySearch(target):
    low = 0
    high = target
    while low <= high:
        mid = (low+high)//2
        mid_sq = mid * mid

        if mid_sq > target:
            high = mid -1

        elif mid_sq < target:
            low = mid+1
    return low -1 

print(SQRUsingBinarySearch(12))
