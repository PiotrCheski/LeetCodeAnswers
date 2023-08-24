from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dictFreq = {}
        for num in nums:
            dictFreq[num] = 1 + dictFreq.get(num, 0)
            if dictFreq.get(num, 0) > len(nums) // 2:
                return num
    

numstest = [3,2,3]
print(Solution().majorityElement(numstest))