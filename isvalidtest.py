class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")": "(",
                       "]":"[", 
                       "}":"{"  }

        for c in s:
            if c in closeToOpen:
                print(c)


s = ""
print(Solution().isValid(s))