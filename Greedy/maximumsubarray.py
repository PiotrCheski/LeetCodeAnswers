nums_test = [1]

def solve(nums):
    res = 0
    sum_of_nums = 0
    for num in nums:
        sum_of_nums += num
        if sum_of_nums < 0:
            sum_of_nums = 0
        else:
            res = max(sum_of_nums, res)
    return res

print(solve(nums_test))