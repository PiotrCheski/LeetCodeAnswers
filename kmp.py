class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        lps = [0] * len(needle)

        prevLPS = 0
        i = 1
        while i < len(needle):
            if needle[i] == needle[prevLPS]:
                lps[i] = prevLPS + 1
                prevLPS += 1
                i += 1
            elif prevLPS == 0:
                lps[i] = 0 
                i += 1
            else:
                prevLPS = lps[prevLPS - 1]
        
        i = 0 # haystack
        j = 0 # needle
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                if j == 0:
                    i += 1
                else:
                    j = lps[j - 1]
            if j == len(needle):
                return i - j
            
        return -1



haystack = "ABCDEF"
needle = "ABC"
print(Solution().strStr(haystack, needle))