from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        if len(flowerbed) == 1:
            if flowerbed[0] == 0 and n == 1:
                return True
            else:
                return False
        
        l = 0
        m = 1
        r = 2
        if flowerbed[0] == 0 and flowerbed[1] == 0:
            n -= 1
            flowerbed[0] = 1
            l += 1
            m += 1
            r += 1

        if flowerbed[len(flowerbed)-2] == 0 and flowerbed[len(flowerbed)-1] == 0:
            n -= 1
            flowerbed[len(flowerbed)-1] = 1

        while r < len(flowerbed):
            if flowerbed[l] == 0 and flowerbed[m] == 0 and flowerbed[r] == 0:
                n -= 1
                flowerbed[m] = 1
                l += 1
                m += 1
                r += 1
            l += 1
            m += 1
            r += 1
        
        if n <= 0:
            return True
        else:
            return False

flowerbedtest = [0,0,1,0,0]
ntest = 1

print(Solution().canPlaceFlowers(flowerbedtest, ntest))