class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        letters = []

        result = []

        for c in columnTitle:
            letters.append(ord(c)-ord("A")+1)
        if len(letters) == 1:
            return letters[0]
        else:
            length = len(letters)

    
testValue = "ZA"
print(Solution().titleToNumber(testValue))