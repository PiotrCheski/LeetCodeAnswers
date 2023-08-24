from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum_of_list = (len(nums)*(len(nums)+1))//2
        sum_of_nums = 0
        for num in nums:
            sum_of_nums += num
        if sum_of_list == sum_of_nums:
            return 0
        else:
            return (sum_of_list - sum_of_nums)


numstest = [3, 0, 1]
print(Solution().missingNumber(numstest))