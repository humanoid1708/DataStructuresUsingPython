def inter(arr1, arr2):
    i = 0
    j = 0
    inter = []
    while i < len(arr1) and j <  len(arr2):
        if arr1[i] == arr2[j] and arr1[i] not in inter:
            inter.append(arr1[i])
            i+=1
            j+=1
        elif arr1[i] < arr2[j]:
            i+=1
        else:
            j+=1

    return inter

A = [1,2,2,4,6,8,9]
B = [2,4,4,5,8,8,9,11]
print(inter(A, B))
