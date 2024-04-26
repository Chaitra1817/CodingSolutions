'''
130. Surrounded Regions
Solved
Medium
Topics
Companies

Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

 

Example 1:

Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation: Notice that an 'O' should not be flipped if:
- It is on the border, or
- It is adjacent to an 'O' that should not be flipped.
The bottom 'O' is on the border, so it is not flipped.
The other three 'O' form a surrounded region, so they are flipped.

'''

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return
        
        m, n = len(board), len(board[0])
        # Create a copy of the board to mark safe 'O's
        safe = [['X' for j in range(n)] for i in range(m)]

        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != 'O':
                return
            
            if safe[r][c] == 'O':  # If already visited, skip to prevent cycles
                return
            
            safe[r][c] = 'O'  # Mark this 'O' as safe
            # Explore all four directions
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # Start DFS from 'O's on the edges
        for i in range(m):
            dfs(i, 0)
            dfs(i, n - 1)
        
        for j in range(n):
            dfs(0, j)
            dfs(m - 1, j)

        # Update the original board using the safe markings
        for i in range(m):
            for j in range(n):
                board[i][j] = safe[i][j]
