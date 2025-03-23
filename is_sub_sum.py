"""
Time complexity : O (n * n )
Aux space : O (1)
"""

def is_subsum(arr:list,sum:int):
    for i in range(len(arr)):
        curr = 0
        for j in range(i,len(arr)):
            curr+=arr[j]
            if curr == sum:
                return True

    return False


if __name__ == "__main__":
    arr = [1,4,20,3,10,5]
    print(is_subsum(arr,sum=33))


"""
sliding window tech
Time complexity : O (n * n )
Aux space : O (1)
"""

def is_subsum(arr:list,sum:int):
    i = 0
    curr = 0

    for k in range(len(arr)):
        curr+=arr[k]
        while curr > sum:
            curr = curr - arr[i]
            i+=1

        if curr == sum:
            return True

    return False

if __name__ == "__main__":
    arr = [1,4,20,3,10,5]
    print(is_subsum(arr,sum=33))

