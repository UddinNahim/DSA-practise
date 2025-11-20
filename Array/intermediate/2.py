"""
🔥 Problem 8 — Two-Sum (Using Hash Map / Dictionary)

Find two numbers that add up to a target.

Example

Array = [2, 7, 11, 15], target = 9
Output = indices (0, 1)

Logic

Use dictionary:

For each number, check if target - num already seen.

If seen → pair found.

Else → store current number in dictionary.

Your Turn:
Array: [3, 8, 2, 7, 11]
Target: 9

Find the two indices that sum to 9.
"""

arr = [2, 7, 11, 15]
target = 16

map = {}

for i in range(len(arr)):
    current = arr[i]
    required = target - current

    print(current,required)
    print(map)

    if required in map:
        print(map[required], i)
        break

    map[current] = i


