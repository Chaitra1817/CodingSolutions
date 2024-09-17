'''
There is an array arr of heights of stone and Geek is standing at the first stone and can jump to one of the following: Stone i+1, i+2, ... i+k stone,
where k is the maximum number of steps that can be jumped and cost will be |hi-hj| is incurred,
where j is the stone to land on. Find the minimum possible total cost incurred before the Geek reaches the last stone.
'''

class Solution:
    def minimizeCost(self, arr, k):
        n=len(arr)
        dp=[float('inf')]*n
        dp[0]=0
        for i in range(1,n):
            mn=float('inf')
            for j in range(1,k+1):
                if i-j>=0:
                    jump=dp[i-j]+abs(arr[i]-arr[i-j])
                    mn=min(mn,jump)
            dp[i]=mn
        return dp[n-1]
