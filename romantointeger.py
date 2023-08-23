class Solution:
    def romanToInt(self, s: str) -> int:
     
        dictOfNums = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        
        num = 0
        
        for i in range(len(s)):
            if i + 1 < len(s) and dictOfNums[s[i]] < dictOfNums[s[i+1]]:
                num -= dictOfNums[s[i]]
            else:
                num += dictOfNums[s[i]]
        return num

sampleroman = "IV"
print(Solution().romanToInt(sampleroman))