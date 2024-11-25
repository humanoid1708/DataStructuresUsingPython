def AddOne(arr):
    arr[-1] += 1
    for i in range(len(arr)-1, -1, -1):
        if arr[i] == 10 and i != 0:
            arr[i-1] += 1
            arr[i] = 0
    if arr[0] == 10:
        arr[0] = 1
        arr.append(0)

    return arr

A = [1,4,9]
print(AddOne(A))
B = [9,9,9,9,9]
print(AddOne(B))
