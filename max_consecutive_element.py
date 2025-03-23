
"""
time complexity -> O(n*k)
"""

def max_cons_element(arr:list,k:int):
    res = float("-inf")

    i = 0
    while i+k-1 < len(arr):
        curr = 0
        for j in range(k):
            curr+=arr[i+j]
        res = max(curr,res)
        i+=1
    return res


if __name__ == "__main__":
    arr = [10,5,-2,20,1]
    print(max_cons_element(arr,k=3))

"""
sliding window tech
"""

def max_consecutive_element(arr:list,k:int):
    curr = 0
    for i in range(k):
        curr+=arr[i]
    res = curr

    for i in range(k,len(arr)):
        curr = curr + arr[i] - arr[i-k]
        res = max(res,curr)

    return res


if __name__ == "__main__":
    arr = [10,5,-2,20,1]
    print(max_consecutive_element(arr,k=3))
