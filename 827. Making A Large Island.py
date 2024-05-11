'''
827. Making A Large Island
Solved
Hard
Topics
Companies

You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.

Return the size of the largest island in grid after applying this operation.

An island is a 4-directionally connected group of 1s.

 

Example 1:

Input: grid = [[1,0],[0,1]]
Output: 3
Explanation: Change one 0 to 1 and connect two 1s, then we get an island with area = 3.

Example 2:

Input: grid = [[1,1],[1,0]]
Output: 4
Explanation: Change the 0 to 1 and make the island bigger, only one island with area = 4.

Example 3:

Input: grid = [[1,1],[1,1]]
Output: 4
Explanation: Can't change any 0 to 1, only one island with area = 4.

 
'''

class Solution:
    def largestIsland(self, grid):
        n = len(grid)
        area = {}
        idx = 2
        
        def dfs(r, c, idx):
            if r < 0 or r >= n or c < 0 or c >= n or grid[r][c] != 1:
                return 0
            grid[r][c] = idx
            result = 1  # Start with the current cell
            directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                result += dfs(nr, nc, idx)  # Accumulate area recursively
            return result

        # Step 1: Calculate areas for all initial islands
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    area[idx] = dfs(i, j, idx)
                    idx += 1

        # Step 2: Try converting a 0 to 1 and calculate potential largest island
        res = max(area.values(), default=0)  # Handle the case of no islands
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    seen = set()
                    for dr, dc in directions:
                        ni, nj = i + dr, j + dc
                        if 0 <= ni < n and 0 <= nj < n:
                            seen.add(grid[ni][nj])
                    temp = 1  # Start with 1 for the current cell
                    for index in seen:
                        if index > 1:
                            temp += area.get(index, 0)
                    res = max(res, temp)

        return res
