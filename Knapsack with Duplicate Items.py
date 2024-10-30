'''
Given a set of N items, each with a weight and a value, represented by the array wt and val respectively. Also, a knapsack with weight limit W.
The task is to fill the knapsack in such a way that we can get the maximum profit. Return the maximum profit.
Note: Each item can be taken any number of times.
'''

# Topdown
class Solution:
    def knapSack(self, N, W, val, wt):
        memo = {}
        def find(idx, total):
            if total > W:
                return float('-inf')
            if idx >= N:
                return 0  # Base case: no more items to consider
            
            if (idx, total) in memo:
                return memo[(idx, total)]
            
            # Option 1: Do not take the item
            notTake = find(idx + 1, total)
            
            # Option 2: Take the item, and we can keep choosing this item again
            take = val[idx] + find(idx, total + wt[idx])
            
            # Store the result in memo
            memo[(idx, total)] = max(notTake, take)
            return memo[(idx, total)]

        # Start the recursion from the 0th item and a total weight of 0
        ans = find(0, 0)
        return ans

# Bottomup
class Solution:
    def knapSack(self, N, W, val, wt):
        # Initialize DP array with 0s, covering all weights from 0 to W inclusive
        dp = [[0 for _ in range(W + 1)] for _ in range(N)]
        
        # Initialize the first row, allowing multiple inclusions of the first item
        for j in range(wt[0], W + 1):
            dp[0][j] = (j // wt[0]) * val[0]
        
        # Fill the DP table
        for i in range(1, N):
            for j in range(1, W + 1):
                # Option 1: Do not take the current item
                notTake = dp[i - 1][j]
                
                # Option 2: Take the current item, as many times as it fits
                take = 0
                if wt[i] <= j:
                    take = val[i] + dp[i][j - wt[i]]
                
                # Maximize the value by taking or not taking the item
                dp[i][j] = max(notTake, take)
        
        # The answer is in dp[N-1][W], the last item and the full capacity
        return dp[N - 1][W]
