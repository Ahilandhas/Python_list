
"""
prefix sum Tech
O(j-i+1)  or O(n)
"""

def get_sum(arr,i,j):
    curr = 0
    for k in range(i,j+1):
        curr+=arr[k]
    return curr

if __name__ == "__main__":
    arr = [2,8,3,9,6,5,4]
    print(get_sum(arr,0,2))



"""
prefix sum Tech
Ouery in O(1) complex time
"""

arr = [2,8,3,9,6,5,4]
n = len(arr)
psum = [None] * n
psum[0] = arr[0]

for i in range(1,n):
    psum[i] = psum[i-1] + arr[i]


def get_sum(arr,i,j):

    if i == 0:
        return psum[j]

    else:
        return psum[j]-psum[i-1]
if __name__ == "__main__":

    print(get_sum(arr,0,2))



"""
Excercise: weighted sum queries
"""

def get_sum(arr,i,j):
    curr = 0
    k = 1
    for i in range(i,j+1):
        curr = curr + (k * arr[i])
        k+=1

   # return curr

if __name__ == "__main__":
    arr = [2,3,5,4,6,1]
    print(get_sum(arr,2,3))
