'''
994. Rotting Oranges
Solved
Medium
Topics
Companies

You are given an m x n grid where each cell can have one of three values:

    0 representing an empty cell,
    1 representing a fresh orange, or
    2 representing a rotten orange.

Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

 

Example 1:

Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

'''

from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        visited = [[0] * n for _ in range(m)]
        queue = deque()
        fresh_fruits = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    visited[i][j] = grid[i][j]
                    queue.append([(i, j), 0])
                if grid[i][j] == 1:
                    fresh_fruits += 1
        tm = 0
        cnt = 0
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        while queue:
            (r, c), t = queue.popleft()
            tm = max(t, tm)
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1 and visited[nr][nc] == 0:
                    visited[nr][nc] = 2
                    cnt += 1
                    queue.append(((nr, nc), t + 1))

        if cnt != fresh_fruits:
            return -1

        return tm

