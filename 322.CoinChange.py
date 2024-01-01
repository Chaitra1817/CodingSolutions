'''
322. Coin Change
Solved
Medium
Topics
Companies

You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

 

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:

Input: coins = [2], amount = 3
Output: -1

Example 3:

Input: coins = [1], amount = 0
Output: 0
'''

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[[-1 for i in range(amount+1)] for i in range(len(coins))]
        def countCoins(ind, target):
            nonlocal coins, dp
            INF = amount + 1

            if ind == 0:
                if target % coins[ind] == 0:
                    return target // coins[ind]
                return INF
            
            if dp[ind][target]!=-1:
                return dp[ind][target]

            notTake = countCoins(ind - 1, target)
            take = INF
            if coins[ind] <= target:
                take = 1 + countCoins(ind, target - coins[ind])

            dp[ind][target]= min(take, notTake)
            return dp[ind][target]

        result = countCoins(len(coins) - 1, amount)
        return -1 if result == amount + 1 else result
