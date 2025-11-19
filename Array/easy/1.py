#Find the largest Element
"""
1.assuming first element is maximum
2. loop through array
3.when find a number greater than current.
        max -> update
4.return max

"""

arr = [5,3,9,2,1,100]

max_value = arr[0]

for i in  arr:
    if max_value < i :
        max_value = i

print("Maximum number is :", max_value)

