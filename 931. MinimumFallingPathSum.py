'''
931. Minimum Falling Path Sum
Medium
Topics
Companies

Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).

 Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
Output: 13
Explanation: There are two falling paths with a minimum sum as shown.

'''

# Code
```
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n=len(matrix)
        dp=[[0 for j in range(n)] for i in range(n)]
        
        for i in range(n):
            for j in range(n):
                if i==0:
                    dp[i][j]=matrix[i][j]
                    continue
                up=matrix[i][j]+dp[i-1][j]
                left=right=float('inf')
                if j>0:
                    left=matrix[i][j]+dp[i-1][j-1]
                if j<n-1:
                    right=matrix[i][j]+dp[i-1][j+1]
                dp[i][j]=min(up,left,right)

        m=float('inf')
        for j in range(n):
            m=min(m,dp[n-1][j])
        return m


        
        # Memoization
        # m=len(matrix)
        # n=len(matrix[0])
        # dp=[[-1 for i in range(n)]for j in range(m)]

        # def findMin(i,j,dp):
        #     nonlocal n
        #     if i<0 or j<0 or j>=n:
        #         return float('inf')
            
        #     if i==0:
        #         return matrix[i][j]
            
        #     if dp[i][j]!=-1:
        #         return dp[i][j]
            
        #     up=matrix[i][j]+findMin(i-1,j,dp)
        #     ld=matrix[i][j]+findMin(i-1,j-1,dp)
        #     rd=matrix[i][j]+findMin(i-1,j+1,dp)

        #     dp[i][j]=min(up,min(ld,rd))
        #     return dp[i][j]
        
        # ans=float('inf')
        # for i in range(n):
        #     ans=min(ans,findMin(m-1,i,dp))

        # return ans
        
```
