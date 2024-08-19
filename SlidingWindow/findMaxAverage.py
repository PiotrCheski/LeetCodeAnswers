def findMaxAverage(nums, k):
    max_sum = sum(nums[:k])
    current_sum = sum(nums[:k])
    for i in range(k, len(nums)):
        current_sum += nums[i] - nums[i-k]
        max_sum = max(max_sum, current_sum)
    return max_sum / k



nums_t = [1,12,-5,-6,50,3]
k_t = 4
print(findMaxAverage(nums_t, k_t))