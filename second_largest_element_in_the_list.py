"""
Naive approch , Required to traversal
"""

def get_sec_max(values):
    if len(values) <= 1:
        return None

    large = get_max(values)
    slarge = None
    for i in range(0,len(values)):
        if values[i] != large:
            if slarge is None:
                slarge = values[i]

            slarge = max(slarge,values[i])

    return slarge

def get_max(values):
    res = values[0]
    for i in range(1,len(values)):
        res = max(res,values[i])
    return res

print(get_sec_max(values))


"""
Efficient way
"""


def get_sec_max(values):
    large = values[0]
    slarge = None


    for x in values:
        if x > large:
            slarge = large
            large  = x
        elif x != large:
            if large == None or x > slarge:
               slarge = x

    return slarge

values = [4,1,3,2,1]
print(get_sec_max(values))
