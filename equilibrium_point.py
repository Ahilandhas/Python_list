"""Equlibrium point"""

"""
time complexity -> O( n * n )
"""
def eqpoint(arr):
    n = len(arr)

    for i in range(n):
        l,r = 0,0
        for j in range(i):
            l+=arr[j]
        for k in range(i+1,n):
            r+=arr[k]

        if l == r:
            return True
    return False


arr = [3,4,8,-9,9,7]
print(eqpoint(arr))

"""
time complexity -> O( n  )
"""

def eqpoint(arr):
    rs = sum (arr)
    ls = 0
    for i in range(len(arr)):
        rs-=arr[i]
        if ls == rs:
            return True
        ls+=arr[i]
    return False

arr = [2,-2,4]
print(eqpoint(arr))
