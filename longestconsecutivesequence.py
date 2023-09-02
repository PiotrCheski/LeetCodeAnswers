from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        res = 1
        max_res = 1
        prevValue = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == prevValue + 1:
                res += 1
            elif nums[i] != prevValue:
                res = 1
            max_res = max(max_res, res)
            prevValue = nums[i]
        return max_res

nums = [-1, -1, 0, 1, 3, 4, 5, 6, 7, 8, 9]
print(Solution().longestConsecutive(nums))