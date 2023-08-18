from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        prevValues = set()
        for number in nums:
            if number in prevValues:
                return True
            prevValues.add(number)
        return False
