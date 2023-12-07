'''
200. Number of Islands
Solved
Medium
Topics
Companies

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

'''
# Ref: https://www.youtube.com/watch?v=__98uL6wst8
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
      if not grid:
        return 0
      
      m,n=len(grid),len(grid[0])
      ans=0

      def dfs(i,j):
        grid[i][j]='2'
        for di,dj in [(0,1),(0,-1),(1,0),(-1,0)]:
          ii,jj=i+di, j+dj
          if 0<=ii <m and 0<=jj<n and grid[ii][jj]=='1':
            dfs(ii,jj)

      for i in range(m):
        for j in range(n):
          if grid[i][j]=='1':
            dfs(i,j)
            ans+=1
      
      return ans
        
