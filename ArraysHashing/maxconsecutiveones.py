def findMaxConsecutiveOnes(nums):
    max_ones = 0
    current_max = 0
    for num in nums:
        if num == 1:
            current_max += 1
        else:
            current_max = 0
        max_ones = max(max_ones, current_max)
    return max_ones



nums_t = [1,1,1,1,1,1]
print(findMaxConsecutiveOnes(nums_t))