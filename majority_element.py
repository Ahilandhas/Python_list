"""
time complexity -> O(n*n)
"""

def majority_of_element(arr:list):
    dict = {element : arr.count(element) for element in arr}
    n = len(arr)
    result = None
    element = None
    if max(dict.values()) > n //2 :
        for elements ,value in dict.items():
            if result is None:
                result = value
                element = elements

            elif value > result:
                result = value
                element = elements

    else:
        return -1

    return arr.index(element)


if __name__ == "__main__":
    arr = [3,8, 4,7,8]
    print(majority_of_element(arr))


def majority_of_element(arr:list):
    n = len(arr)
    for i in range(n):
        count = 1
        for j in range(i+1,n):
            if arr[i] == arr[j]:
                count+=1

        if count > n // 2 :
            return i

    return -1

if __name__ == "__main__":
    arr = [3,8, 4,7,8]
    print(majority_of_element(arr))
