"""
Maximum difference
-> Naive approch

Time complexity -> o(n *2 )
"""

def maximum_difference(arr:list) -> int:
    res = arr[1] - arr[0]

    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            res = max(res,arr[j]-arr[i])

    return res

arr = [2,3,10,6,4,8,1]
print(maximum_difference(arr))

"""
Maximum difference
-> Efficient approch
Time complexity -> o(n)
"""
def maximum_difference(arr:list) -> int:
    res = arr[1] - arr[0]
    min_value = arr[0]
    for j in range(1,len(arr)):
        res = max(res,arr[j]-min_value)
        min_value = min(min_value,arr[j])

    return res

arr = [2,1,10,6,4,8,1]
print(maximum_difference(arr))
