'''
741. Cherry Pickup
Solved
Hard
Topics
Companies

You are given an n x n grid representing a field of cherries, each cell is one of three possible integers.

    0 means the cell is empty, so you can pass through,
    1 means the cell contains a cherry that you can pick up and pass through, or
    -1 means the cell contains a thorn that blocks your way.

Return the maximum number of cherries you can collect by following the rules below:

    Starting at the position (0, 0) and reaching (n - 1, n - 1) by moving right or down through valid path cells (cells with value 0 or 1).
    After reaching (n - 1, n - 1), returning to (0, 0) by moving left or up through valid path cells.
    When passing through a path cell containing a cherry, you pick it up, and the cell becomes an empty cell 0.
    If there is no valid path between (0, 0) and (n - 1, n - 1), then no cherries can be collected.

 

Example 1:

Input: grid = [[0,1,-1],[1,0,-1],[1,1,1]]
Output: 5
Explanation: The player started at (0, 0) and went down, down, right right to reach (2, 2).
4 cherries were picked up during this single trip, and the matrix becomes [[0,1,-1],[0,0,-1],[0,0,0]].
Then, the player went left, up, up, left to return home, picking up one more cherry.
The total number of cherries picked up is 5, and this is the maximum possible.

Example 2:

Input: grid = [[1,1,-1],[1,-1,1],[-1,1,1]]
Output: 0

'''

from typing import List

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        memo = {}  # Memoization dictionary

        def find(i1, j1, i2, j2):
            # Check if already memoized
            if (i1, j1, i2, j2) in memo:
                return memo[(i1, j1, i2, j2)]

            # Base case: reached bottom-right corner
            if i1 == m - 1 and j1 == n - 1 and i2 == m - 1 and j2 == n - 1:
                return grid[m - 1][n - 1]

            # Check if out of bounds or blocked cells
            if i1 >= m or j1 >= n or i2 >= m or j2 >= n or grid[i1][j1] == -1 or grid[i2][j2] == -1:
                return float('-inf')

            # Count cherries picked up at current cells
            cherries = grid[i1][j1] + (grid[i2][j2] if (i1, j1) != (i2, j2) else 0)

            # Explore all possible moves and pick the maximum cherries
            result = max(
                find(i1 + 1, j1, i2 + 1, j2),
                find(i1 + 1, j1, i2, j2 + 1),
                find(i1, j1 + 1, i2 + 1, j2),
                find(i1, j1 + 1, i2, j2 + 1)
            ) + cherries

            # Memoize the result
            memo[(i1, j1, i2, j2)] = result

            return result

        # Start DFS from (0, 0) and (0, 0)
        return max(0, find(0, 0, 0, 0))
