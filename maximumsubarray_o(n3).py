from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        for i in range(0, len(nums)):
            currSum = 0
            for j in range(i, len(nums)):
                currSum += nums[j]            
                maxSum = max(maxSum, currSum)
        return maxSum


testlist = [-1]
testsolution = Solution().maxSubArray(testlist)
print(testsolution)