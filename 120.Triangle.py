'''
120. Triangle
Solved
Medium
Topics
Companies

Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

 

Example 1:

Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).

Example 2:

Input: triangle = [[-10]]
Output: -10

 '''

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        n=len(triangle)
        dp=[[-1 for i in range (n)] for i in range(n)]
        def minPath(i,j):
            nonlocal triangle
            if i>=n or j>=n:
                return 0
            
            if i==n-1:
                return triangle[i][j]
            
            if dp[i][j]!=-1:
                return dp[i][j]
            
            d= triangle[i][j] + minPath(i+1,j)
            dg = triangle[i][j] + minPath(i+1,j+1)
            
            dp[i][j] = min(d,dg)
            return dp[i][j]
        
        return minPath(0,0)
            

        
