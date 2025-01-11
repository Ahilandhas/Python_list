"""

left rotate by one in list

"""

values = [1,2,3,4,5]

"""
Direct method
"""

values = values[1:] + values[:1]

print(values)

values = [1,2,3,4,5]

values.append(values.pop(0))

print(values)

"""
own logic
"""

value = values[0]
for i in range(0,len(values)-1):
    print(i)
    values[i] = values[i+1]
values[len(values)-1] = value

print(values)
