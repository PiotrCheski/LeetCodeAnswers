nums_test = [5, 4, 2, 3]

def solve(nums):
    nums.sort()
    for i in range(len(nums)-1):
        if i % 2 == 0:
            tmp = nums[i]
            nums[i] = nums[i+1]
            nums[i+1] = tmp
    return nums

print(solve(nums_test))