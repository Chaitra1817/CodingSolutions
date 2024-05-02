'''
695. Max Area of Island
Solved
Medium
Topics
Companies

You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

 

Example 1:

Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.

'''

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r >= m or c >= n or grid[r][c] != 1:
                return 0
                        
            grid[r][c] = 2  # Mark as visited to prevent revisiting
            res = 1  # Count the current cell in the area
            directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]  # Up, Right, Down, Left
            for dr, dc in directions:
                res += dfs(r + dr, c + dc)
            
            return res

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:  # Start DFS only if the cell is part of an unvisited island
                    cur = dfs(i, j)
                    ans = max(ans, cur)

        return ans
