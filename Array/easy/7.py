"""
🔥 Problem 4 — Move Zeros to the End

Example:
Input: [0, 3, 0, 5, 7]
Output: [3, 5, 7, 0, 0]

🔥 Logic

Keep a pointer pos = 0 for the next non-zero element.

Traverse array:

If element ≠ 0 → place it at arr[pos], then pos++.

Fill remaining positions with 0.

This builds two-pointer and rearrangement thinking, super important for many array problems.

Your Turn: Move zeros in:

[0, 1, 0, 2, 0, 3]
"""


arr = [0, 3, 0, 5, 7]

pos = 0  # pointer for next non-zero position

# Step 1: Move all non-zero elements to the front
for num in arr:  # num is the element itself
    if num != 0:
        arr[pos] = num
        pos += 1
        print(pos)



# Step 2: Fill remaining positions with 0
for i in range(pos, len(arr)):
    arr[i] = 0

# Result
print("Array after moving zeros:", arr)





