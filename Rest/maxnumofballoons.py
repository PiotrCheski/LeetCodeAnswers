from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        countText = Counter(text)
        ballon = Counter("balloon")

        res = len(text)
        for char in ballon:
            res = min(res, countText[char] // ballon[char])
        return res
    
        
text = "nlaebolko"
print(Solution().maxNumberOfBalloons(text))