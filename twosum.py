from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # hashmap value : index
        for i, n in enumerate(nums): #enumerate nums list to get index and value
            difference = target - n
            if difference in prevMap:
                return [prevMap[difference], i]
            prevMap[n] = i
        return None