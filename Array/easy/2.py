"""
✅ Problem 2 — Find the Minimum Number in an Array
Example:

Input:
[4, 9, 2, 7]
Output : 2

"""

arr = [14, 3, 22, 1, 9, 7]

min_value = arr[0]

for  num in arr:
    if  num < min_value  :
        min_value = num

print("minimum numbers :" , min_value)

