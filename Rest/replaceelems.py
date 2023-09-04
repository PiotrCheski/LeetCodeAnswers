from typing import List

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rightMax = -1

        for i in range(len(arr)-1, -1, -1):
            newMax = max(rightMax, arr[i])
            arr[i] = rightMax
            rightMax = newMax
        return arr


nums = [1, 17,19,20,21,22]

print(Solution().replaceElements(nums))