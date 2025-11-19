"""
🔥 Problem 6 — Check if Array is Sorted

Example:
Input: [1, 2, 3, 4] → Output: True
Input: [1, 3, 2] → Output: False

🔥 Logic

Traverse from 0 → n-2

If arr[i] > arr[i+1] → return False

If loop completes → True

Your Turn: Check if this array is sorted:

[2, 4, 5, 7, 6]
"""

arr = [1, 2,5, 3, 4 , 8]

is_sorted = True
for i in range(len(arr) -1):
    if arr[i] > arr[i + 1]:
        is_sorted = False
        break


print(is_sorted)