class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            match = True  # Assume a match initially
            for j in range(len(needle)):
                if haystack[i + j] != needle[j]:
                    match = False
                    break
            if match:
                return i
        return -1



haystack = "ABCDEF"
needle = "ABC"
print(Solution().strStr(haystack, needle))