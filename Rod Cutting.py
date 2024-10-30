'''
Given a rod of length N inches and an array of prices, price[]. price[i] denotes the value of a piece of length i. Determine the maximum value obtainable by cutting up the rod and selling the pieces.

Note: Consider 1-based indexing.

'''

# #User function Template for python3

class Solution:
    def cutRod(self, price, n):
        #code here
        memo={}
        def find(idx,total):
            if total>n or idx>=n:
                return float('-inf')
            if total==n:
                return 0

            if(idx,total) in memo:
                return memo[(idx,total)]
            notTake=find(idx+1,total)
            take=price[idx]+find(idx,total+idx+1)
            
            memo[(idx,total)]= max(take,notTake)
            return memo[(idx,total)]
            
        return find(0,0)

#User function Template for python3
class Solution:
    def cutRod(self, price, n):
        # DP array to store the maximum profit for each rod length from 0 to n
        dp = [0] * (n + 1)

        # Build the dp array from length 1 to n
        for length in range(1, n + 1):
            max_val = float('-inf')
            # Try each cut from 1 to current length
            for cut in range(1, length + 1):
                # Update max_val by considering the current cut
                max_val = max(max_val, price[cut - 1] + dp[length - cut])
            dp[length] = max_val  # Store the maximum profit for this length

        # The last entry contains the maximum profit for a rod of length n
        return dp[n]
