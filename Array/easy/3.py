"""
✅ Problem 3 — Count Even Numbers in an Array

Example:
Input: [2, 5, 7, 8, 10]
Output: 3 (because 2, 8, 10)

"""

arr = [2, 5, 7, 8, 10]
count_even = 0

for i in arr:
    if i % 2 == 0:
        count_even += 1

print("The total even number", count_even)


