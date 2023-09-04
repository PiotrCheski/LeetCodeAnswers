from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        leftProducts = [0] * len(nums)
        rightProducts = [0] * len(nums)

        leftProducts[0] = 1
        rightProducts[len(nums)-1] = 1

        for i in range(1, len(nums)):
            leftProducts[i] = nums[i-1] * leftProducts[i-1]
        
        for i in range(len(nums)-2, -1, -1):
            rightProducts[i] = nums[i+1] * rightProducts[i+1]
        
        for i in range(len(nums)):
            res[i] = leftProducts[i] * rightProducts[i]
        return res





testlist = [4, 5, 1, 8, 2]
testsolution = Solution().productExceptSelf(testlist)
print(testsolution)