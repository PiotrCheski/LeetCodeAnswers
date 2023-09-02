from typing import List

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        product = nums[0]

        for i in range(1, len(nums)):
            product *= nums[i]
        
        res = self.signFunc(product)
        return res

    def signFunc(self, x):
        if x > 0:
            return 1
        elif x < 0:
            return -1
        else:
            return 0
        
nums = [-1,-2,-3,-4,3,2,1]
print(Solution().arraySign(nums))