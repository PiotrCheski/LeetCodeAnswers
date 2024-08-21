def uniqueOccurrences(arr):
    hash_set = {}
    unique_values = set()
    for num in arr:
        if num not in hash_set:
            hash_set[num] = 1
        else:
            hash_set[num] += 1
    for value in hash_set.values():
        if value not in unique_values:
            unique_values.add(value)
        else:
            return False
    return True

arr_t = [1,2,2,1,1,3]
print(uniqueOccurrences(arr_t))