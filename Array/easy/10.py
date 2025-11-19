# Count duplicates in the array.


arr = [1,2,2,2,3,3,4]

count_dict = {}
count = 0

for i in arr:
    if i in count_dict:
        count_dict[i] += 1
    else:
        count_dict[i] = 1

print(count_dict)

duplicate_count = 0

for key in count_dict:
    if count_dict[key] > 1:
        duplicate_count += 1

print(duplicate_count)