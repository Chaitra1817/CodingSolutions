'''
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.

 

Example 1:

Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]

'''

from typing import List
from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        q = deque()
        
        # Initialize distances with inf, except the cells with 0, which are set to 0
        distances = [[float('inf')] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i, j))
                    distances[i][j] = 0

        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # up, right, down, left
        while q:
            row, col = q.popleft()
            current_distance = distances[row][col]
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < m and 0 <= new_col < n:
                    if distances[new_row][new_col] == float('inf'):  # Not visited
                        distances[new_row][new_col] = current_distance + 1
                        q.append((new_row, new_col))

        return distances
