'''
1020. Number of Enclaves
Solved
Medium
Topics
Companies
Hint

You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.

A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.

Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.
 

Example 1:

Input: grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
Output: 3
Explanation: There are three 1s that are enclosed by 0s, and one 1 that is not enclosed because its on the boundary.

Example 2:

Input: grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
Output: 0
Explanation: All 1s are either on the boundary or can reach the boundary.


Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 500
    grid[i][j] is either 0 or 1.


'''

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])

        def dfs(r,c):
            if r<0 or c<0 or r>=m or c>=n or grid[r][c]!=1:
                return
            
            grid[r][c]=2
            dir=[[-1,0],[0,1],[1,0],[0,-1]]
            for nr,nc in dir:
                dfs(nr+r,nc+c)
        
        for i in range(m):
            dfs(i,0)
            dfs(i,n-1)
        
        for j in range(n):
            dfs(0,j)
            dfs(m-1,j)
        
        ans=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    ans+=1

        return ans        
        

