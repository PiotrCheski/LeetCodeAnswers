class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            xstring = str(x)
            reverse_xstring = ''
            for char in xstring[::-1]:
                reverse_xstring += char

            if xstring == reverse_xstring:
                return True
            return False
    
testx = 101
print(Solution().isPalindrome(testx))