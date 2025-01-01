

values = [10,20,20,30,10]

def is_sorted(values):
    if len(values) < 2:
        return True

    for i in range(0,len(values)-1):
        if values[i] <= values[i+1]:
            continue
        else:
            return False
    return True
"""
Efficient method
"""

def is_sorted(values):
    i = 1
    while i < len(values):
        if values[i] < values[i-1]:
            return False
        i+=1

    return True

def is_sorted(values):
    sort_values = sorted(values)
    if sort_values == values:
        return True
    return False

print(is_sorted(values))
