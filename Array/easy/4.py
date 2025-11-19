"""
✅ Problem 3 — Find the Index of a Target Element

Example:
Array: [10, 20, 30]
Target: 20
Output: 1

"""
arr =  [3, 8, 2, 15, 9, 12]
target = 15


for i in range(len(arr)):
    if arr[i] == target:
        print("target found at index :" , i)
        break
    else:
            print("target not found")




