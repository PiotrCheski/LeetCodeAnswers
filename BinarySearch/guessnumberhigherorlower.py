# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l = 1
        while l <= n:
            mid = (l + n) // 2
            my_guess = guess(mid)
            if my_guess == -1:
                n = mid - 1
            elif my_guess == 1:
                l = mid + 1
            elif my_guess == 0:
                return mid 