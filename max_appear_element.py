
"""
maximum Appearing Element in Ranges
"""

left = [1,2]
right = [5,4]

def max_appearing_element(left,right):
    dict = {}

    k = 0
    while k < len(right):
        i = left[k]
        j = right[k]

        for i in range(i,j+1):
            if i not in dict:
                dict[i] = 1
            else:
                dict[i]+=1
        k+=1

    max_value = 0
    element = 0
    for key,value in dict.items():
        if value > max_value:
            max_value = value
            element = key


    return element

print(max_appearing_element(left,right))

"""
O(n * max)
"""

def max_appear(left,right):
    freq = [0] * 100
    for i in range(len(left)):
        for j in range(left[i],right[i]+1):
            freq[j]+=1
    return freq.index(max(freq))


left = [1,2]
right = [5,4]
print(max_appear(left,right))

"""
O(n + max)
"""

def max_appear(left,right):
    freq = [0] * 100
    for i in range(len(left)):
        freq[left[i]]+=1
        freq[right[i]+1]-=1

    for i in range(1,100):
        freq[i] = freq[i]+ freq[i-1]

    return freq.index(max(freq))
