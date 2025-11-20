"""
🔥 Problem 7 — Find Second Largest Element

Example:
Input: [5, 1, 9, 3]
Output: 5 (largest = 9, second largest = 5)

Logic to Think

Track max1 (largest) and max2 (second largest).

Traverse array:

If current > max1 → update both

Else if current > max2 and current != max1 → update max2
"""


arr = [ 1, 9, 3,4,11]
max1 = float('-inf')
max2 = float('-inf')

for i in arr:
    if i > max1:
        max2 = max1
        max1 = i
        print(max1)
    elif i > max2 and i != max1:
        max2 = i 

        

print(max2)
