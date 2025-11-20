arr = [1, -2, 3, 5, -3]

current_sum =  0
max_sum = float('-inf')

for i in arr:
    current_sum += i
    if current_sum > max_sum:
        current_sum = max_sum
    if current_sum < 0 :
        max_sum = 0

print(max_sum)



