from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0 
        for n in nums:
            res = n ^ res
            print(res)

numstest = [4,1,2,1,2]
print(Solution().singleNumber(numstest))
