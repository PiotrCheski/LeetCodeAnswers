from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)  # Sort the coins in descending order
        num_of_coins = [0] * len(coins)

        for i, coin in enumerate(coins):
            num_of_coins[i] = amount // coin
            amount -= num_of_coins[i] * coin

        if amount == 0:
            for i, coin in enumerate(coins):
                print(f'Num of {coin}: {num_of_coins[i]}')
            return sum(num_of_coins)
        else:
            return -1

testcoins = [1,5,10,20]
testamount = 36

print(Solution().coinChange(testcoins, testamount))