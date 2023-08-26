from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l+r) // 2

            if nums[mid] == target:
                return mid

            if target > nums[mid]:
                l = mid + 1
            if target < nums[mid]:
                r = mid - 1

        return l

    
numstest = [1, 3, 5, 6]
targettest = 2

print(Solution().searchInsert(numstest, targettest))