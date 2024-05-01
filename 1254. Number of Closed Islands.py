'''
1254. Number of Closed Islands
Solved
Medium
Topics
Companies
Hint

Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

Return the number of closed islands.

 

Example 1:

Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
Output: 2
Explanation: 
Islands in gray are closed because they are completely surrounded by water (group of 1s).

'''

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        cnt = 0

        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n:
                return False  # Out of bounds - not a closed island
            
            if grid[r][c] != 0:
                return True  # Either already visited or it's a '1'
            
            grid[r][c] = 2  # Mark as visited
            is_closed = True
            directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            for dr, dc in directions:
                if not dfs(r + dr, c + dc):
                    is_closed = False
            
            return is_closed

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0 and dfs(r, c):
                    cnt += 1

        return cnt
