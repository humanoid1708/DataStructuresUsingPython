def Advance(arr):
    reach = 0
    end = len(arr) - 1
    i = 0
    while i <= reach and reach < end:
        reach = max(reach, arr[i] + i)
        i += 1
    return reach >= end

A = [3,3,1,0,2,0,1]
print(Advance(A))
B = [3,2,0,0,2,0,1]
print(Advance(B))