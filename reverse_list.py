

"""
reverse a list -> own method
"""

values = [10,20,20,30,10]

def reverse_list(values):
    i = 0
    j = len(values)-1

    while i < j :
        values[i],values[j] = values[j],values[i]
        i+=1
        j-=1

reverse_list(values)

print(values)
