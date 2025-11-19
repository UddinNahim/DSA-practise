"""
✅ Example:

Input: [1, 2, 3, 4]
Output: [4, 3, 2, 1]



"""


arr = [1,2,3,5]

start = 0
end = len(arr) - 1

while start < end :
    arr[start] , arr[end]  = arr[end] , arr[start]
    start +=1
    end -= 1

print(arr)
