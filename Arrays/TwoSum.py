def CheckSum(arr, target):
    i = 0
    j = len(arr)-1
    while i < j:
        if arr[i] + arr[j] == target:
            print(str(arr[i]) + "," + str(arr[j]))
            return True

        elif arr[i] + arr[j] < target:
            i += 1

        else:
            j -= 1
    return False
A = [-2, 1, 2, 4, 7, 11]
target = 11
CheckSum(A, target)           