from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while l < r:
            sum_ofLR = numbers[l] + numbers[r]
            if sum_ofLR == target:
                return [l+1, r+1]
            if sum_ofLR > target:
                r -= 1
            else:
                l += 1
            
numberstest = [2,7,11,15]
targettest = 9
print(Solution().twoSum(numberstest, targettest))