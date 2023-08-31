class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters = set()
        maxInt = 0
        for i in range(len(s)):
            l = i
            currInt = 0
            while l <= len(s)-1:
                if s[l] not in letters:
                    letters.add(s[l])
                    currInt += 1
                    l += 1
                elif s[l] in letters:
                    letters.clear()
                    break
            maxInt = max(maxInt, currInt)
        return maxInt



t="abcda"
print(Solution().lengthOfLongestSubstring(t))