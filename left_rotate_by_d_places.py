
"""
Left rotate by d places
"""
# Direct methods

d = 2
l = [1,2,3,4,5]

l = l[d:] + l[:d]

print(l)


"""
own method
Time complexity theta(nd)
"""
values = [1,2,3,4,5]
d = 2
def letf_rotate_n(values,d):
    for i in range(d):
        values.append(values.pop(0))

    print(values)


letf_rotate_n(values,d)

"""
optimized solution
theta(n) and constant auxillary space

-> reversing first d numbers
-> then reversing after d numbers
-> last reversing all numbers
"""
values = [1,2,3,4,5]

def letf_rotate_n(values,d):
    n = len(values)-1
    reverse(0,d-1)
    reverse(d,n)
    reverse(0,n)

def reverse(low,high):
    while low < high:
        values[low],values[high] = values[high],values[low]
        low+=1
        high-=1


letf_rotate_n(values,d)
print(values)
