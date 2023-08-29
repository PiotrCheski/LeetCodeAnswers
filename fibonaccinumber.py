class Solution:
    def fib(self, n: int) -> int:

        computed = {0 : 0,
                    1: 1}
        
        if n not in computed:
            computed[n] = self.fib(n-1) + self.fib(n-2)
        return computed[n]

testn = 4
print(Solution().fib(testn))