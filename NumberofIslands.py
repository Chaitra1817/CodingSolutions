'''
Given an m x n 2d grid map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

#python code

'''


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
		# count of number of islands
        count=0
        row=len(grid)
        col=len(grid[0])
        	# iterate through the grid
        for i in range(row):
            for j in range(col):
                			# if part of island, mark the entire island
                if grid[i][j]=="1":
                    count+=1
                    self.dfs(grid,i,j)
        return count
    
    def dfs(self,grid,i,j):
                # using a simple BST approach, marking visited parts of an island as 0
        if(i<0 or j<0 or i>=len(grid) or j>=len(grid[0])):
            return 
        if grid[i][j]=="0":
            return
         
		# mark a visited part of the island as 0
        grid[i][j]="0"
        self.dfs(grid,i+1,j)
        self.dfs(grid,i-1,j)
        self.dfs(grid,i,j+1)
        self.dfs(grid,i,j-1)
        
 