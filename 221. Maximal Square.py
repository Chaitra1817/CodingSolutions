'''

Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

 

Example 1:

Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4

'''

from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        grid = [[0] * (n + 1) for _ in range(m + 1)]  
        max_side = 0  
        
        for i in range(1, m + 1):  
            for j in range(1, n + 1):
                if matrix[i - 1][j - 1] == "1": 
                    grid[i][j] = min(grid[i - 1][j], grid[i][j - 1], grid[i - 1][j - 1]) + 1
                    max_side = max(max_side, grid[i][j])  
        
        return max_side ** 2  
