class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = {}

        for c in s:
            if c in letters:
                letters[c] += 1
            else:
                letters[c] = 1
        for c in t:
            if c in letters:
                letters[c] -= 1
            else:
                letters[c] = 1

        print(letters)

        if any(letters.values()):
            return False
        else:
            return True



s = "a"
t = "ab"
print(Solution().isAnagram(s, t))
