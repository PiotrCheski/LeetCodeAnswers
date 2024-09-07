def arrayPairSum(nums):
    nums.sort()
    sum_result = 0
    for i in range(0, len(nums), 2):
        sum_result += nums[i]
    return sum_result

nums_t = [1,4,3,2]
print(arrayPairSum)