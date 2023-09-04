class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        letters = [0] * 26  # Assuming only lowercase English letters
        for i in range(len(s)):
            letters[ord(s[i]) - ord("a")] += 1
            letters[ord(t[i]) - ord("a")] -= 1

        return all(count == 0 for count in letters)

s = "rat"
t = "taar"
print(Solution().isAnagram(s, t))
