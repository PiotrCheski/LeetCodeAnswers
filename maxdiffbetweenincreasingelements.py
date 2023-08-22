from typing import List

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        maxDiff = -1
        left_pointer, right_pointer = 0, 1
        while right_pointer < len(nums):
            if nums[left_pointer] < nums[right_pointer]:
                currDiff = nums[right_pointer] - nums[left_pointer]
                maxDiff = max(maxDiff, currDiff)
            else:
                left_pointer = right_pointer
            right_pointer += 1
        return maxDiff
    

nums = [7,1,5,4]
print(Solution().maximumDifference(nums))