class Solution:
    def getSum(self, a: int, b: int) -> int:

        mask = 0xffffffff

        while (b & mask) > 0:
            tmp = (a & b) << 1
            a = (a ^ b)
            b = tmp
        return (a & mask) if b > 0 else a

atest = 1
btest = 2
print(Solution().getSum(atest, btest))