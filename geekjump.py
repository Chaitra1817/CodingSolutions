'''
 Geek wants to climb from the 0th stair to the (n-1)th stair. At a time the Geek can climb either one or two steps. A height[N] array is also given.
 Whenever the geek jumps from stair i to stair j, the energy consumed in the jump is abs(height[i]- height[j]), 
 where abs() means the absolute difference. return the minimum energy that can be used by the Geek to jump from stair 0 to stair N-1.

 '''
class Solution:
    def minimumEnergy(self, height, n):
        dp=[float('inf')]*n
        dp[0]=0
        for i in range(1,n):
            f=dp[i-1]+abs(height[i]-height[i-1])
            s=float('inf')
            if i>1:
                s=dp[i-2]+abs(height[i]-height[i-2])
            dp[i]=min(f,s)
        return dp[n-1]
