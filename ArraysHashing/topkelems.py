from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)]
        res = []

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        for num, c in count.items():
            freq[c].append(num)

        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res  

nums = [2, 2, 1, 1]
k = 2
print(Solution().topKFrequent(nums, k))