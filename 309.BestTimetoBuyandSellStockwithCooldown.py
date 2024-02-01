'''

309. Best Time to Buy and Sell Stock with Cooldown
Solved
Medium
Topics
Companies

You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

    After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

Example 1:

Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]

Example 2:

Input: prices = [1]
Output: 0

 

Constraints:

    1 <= prices.length <= 5000
    0 <= prices[i] <= 1000

'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        memo={}
        def find(i,buy):
            nonlocal prices,memo
            if(i>=len(prices)):
                return 0
            if (i,buy) in memo:
                return memo[(i,buy)]
            if(buy):
                profit=max(-prices[i]+find(i+1,0),find(i+1,1))
            else:
                profit=max(prices[i]+find(i+2,1),find(i+1,0))
            
            memo[(i,buy)]=profit
            return memo[(i,buy)]
        
        return find(0,1)
