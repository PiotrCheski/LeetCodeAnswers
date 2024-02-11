def can_jump(nums):
    end = len(nums) - 1

    for i in range(len(nums)-1, -1, -1):
        if i + nums[i] >= end:
            end = i
    if end == 0:
        return True
    return False

# Example usage:
nums = [2, 2, 0, 1]
result = can_jump(nums)
print(result)
