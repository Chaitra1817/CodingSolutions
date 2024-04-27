'''
1091. Shortest Path in Binary Matrix
Solved
Medium
Topics
Companies
Hint

Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

    All the visited cells of the path are 0.
    All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).

The length of a clear path is the number of visited cells of this path.

 

Example 1:

Input: grid = [[0,1],[1,0]]
Output: 2

'''

from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        if grid[0][0] != 0 or grid[m-1][n-1] != 0:
            return -1

        queue = deque([(0, 0, 1)])  # (row, col, distance)
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1), (-1, -1), (-1, 1), (1, 1), (1, -1)]
        
        while queue:
            row, col, dist = queue.popleft()
            
            if row == m - 1 and col == n - 1:
                return dist
            
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if 0 <= r < m and 0 <= c < n and grid[r][c] == 0:
                    grid[r][c] = 1  # mark as visited by changing the value to 1
                    queue.append((r, c, dist + 1))
        
        return -1
