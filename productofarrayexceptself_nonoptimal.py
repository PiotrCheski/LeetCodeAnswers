from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix_table = [1] *len(nums)
        prefix = 1
        for i in range(len(nums)):
            prefix *= nums[i]
            prefix_table[i] = prefix
            
        postfix_table = [1] *len(nums)
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            postfix *= nums[i]
            postfix_table[i] = postfix

        res = [1] * len(nums)

        for i in range(len(nums)):
            left_product = prefix_table[i-1] if i > 0 else 1
            right_product = postfix_table[i+1] if i < len(nums) - 1 else 1
            res[i] = left_product * right_product
        return res


testlist = [1, 2, 3, 4]
testsolution = Solution().productExceptSelf(testlist)
print(testsolution)