'''
62. Unique Paths
Solved
Medium
Topics
Companies

There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.


Example 1:

Input: m = 3, n = 7
Output: 28

Example 2:

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

'''
# Memoization
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[-1 for i in range(n)] for j in range(m)]
        def findPaths(row,col):
            if row==0 and col==0:
                dp[row][col]=1
                return dp[row][col]
                
            if row<0 or col<0:
                return 0
            
            if dp[row][col]!= -1:
                return dp[row][col]

            up=findPaths(row-1,col)
            left=findPaths(row,col-1)
            
            dp[row][col]=up+left
            return dp[row][col]
        
        return findPaths(m-1,n-1)



        
# Tabulation
        dp=[[-1 for i in range(n)]for j in range(m)]

        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    dp[i][j]=1
                else:
                    up=0
                    left=0
                    if i>0:
                        up=dp[i-1][j]
                    if j>0:
                        left=dp[i][j-1]
                    
                    dp[i][j]=up+left
        
        return dp[m-1][n-1]
