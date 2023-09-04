from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        leftpointer = 0
        rightpointer = len(height)-1

        for h in height:
            currArea = (rightpointer - leftpointer) * min(height[leftpointer], height[rightpointer])
            maxArea = max(maxArea, currArea)
            if height[leftpointer] < height[rightpointer]:
                leftpointer += 1
            else:
                rightpointer -= 1
        return maxArea

heighttesst = [1,8,6,2,5,4,8,3,7]
print(Solution().maxArea(heighttesst))