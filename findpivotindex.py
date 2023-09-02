from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum_of_nums = 0
        sum_of_pp = 0
        for num in nums:
            sum_of_nums += num

        for i in range(len(nums)):
             sum_of_nums -= nums[i]
             if sum_of_pp == sum_of_nums:
                  return i
             else:
                  sum_of_pp += nums[i]
        return -1



nums = [-1,-1,0,1,1,0]
print(Solution().pivotIndex(nums))