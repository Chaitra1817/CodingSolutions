'''
Description
Editorial
Editorial
Solutions
Solutions
Submissions
Submissions
Accepted
Accepted
Code
Testcase
Testcase
Test Result
64. Minimum Path Sum
Solved
Medium
Topics
Companies

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.


Example 1:

Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

Example 2:

Input: grid = [[1,2,3],[4,5,6]]
Output: 12

'''

from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp=[[-1 for i in range(n)] for j in range(m)]

        def minPath(row, col,dp):
            if row < 0 or col < 0:
                return float('inf')  

            if row == 0 and col == 0:
                return grid[row][col]
        
            if dp[row][col]!=-1:
                return dp[row][col]

            up = minPath(row - 1, col, dp)
            left = minPath(row, col - 1, dp)

            dp[row][col] = grid[row][col] + min(up, left)
            return dp[row][col]

        return minPath(m - 1, n - 1,dp)

# Tabulation

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[-1 for i in range(n)] for i in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = grid[0][0]
                else:
                    up, left = float('inf'), float('inf')  
                    if i > 0:
                        up = dp[i - 1][j]
                    if j > 0:
                        left = dp[i][j - 1]
                    dp[i][j] = min(up, left) + grid[i][j]

        return dp[m - 1][n - 1]
