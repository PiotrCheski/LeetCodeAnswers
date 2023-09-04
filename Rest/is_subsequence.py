from typing import List
from collections import defaultdict

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        
        l = 0
        res = []

        for i in range(len(t)):
            if s[l] == t[i]:
                res.append(1)
                if len(res) == len(s):
                    return True
                l += 1
        return False

        #while l <= r:
        #    if s[l] == t[l]:
        #        res.append(1)
        #        l += 1

s="badd"
t="abcddd"

print(Solution().isSubsequence(s, t))