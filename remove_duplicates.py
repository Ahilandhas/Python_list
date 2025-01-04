"""
Remove duplicates from un sorted array

"""

a = [1, 2, 2, 3, 4, 4, 5]

# Create an empty list to store unique values
res = []

# Iterate through each value in the list 'a'
for val in a:

    # Check if the value is not already in 'res'
    if val not in res:
        # If not present, append it to 'res'
        res.append(val)

print(res)

"""
List comprehension
"""

a = [1, 2, 2, 3, 4, 4, 5]

# Create an empty list to store unique values
res = []

# Use list comprehension to append values to 'res'
# if they are not already present
[res.append(val) for val in a if val not in res]

print(res)


"""
using dict
"""

a = [1, 2, 2, 3, 4, 4, 5]

# Remove duplicates using dictionary fromkeys()
a = list(dict.fromkeys(a))

print(a)
