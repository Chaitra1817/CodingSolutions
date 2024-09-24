'''
You are given an n rows and m cols matrix grid representing a field of chocolates where grid[i][j] represents the number of chocolates that you can collect from the (i, j) cell.

You have two robots that can collect chocolates for you:

    Robot #1 is located at the top-left corner (0, 0), and
    Robot #2 is located at the top-right corner (0, cols - 1).

Return the maximum number of chocolates collection using both robots by following the rules below:

    From a cell (i, j), robots can move to cell (i + 1, j - 1), (i + 1, j), or (i + 1, j + 1).
    When any robot passes through a cell, It picks up all chocolates, and the cell becomes an empty cell.
    When both robots stay in the same cell, only one takes the chocolates.
    Both robots cannot move outside of the grid at any moment.
    Both robots should reach the bottom row in grid.

'''
class Solution:
    def solve(self, m, n, grid):
        # 3D dp table [m][n][n], where m is rows, and n is columns
        dp = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(m)]
        
        # Initialize the base case for the last row
        for j1 in range(n):
            for j2 in range(n):
                if j1 == j2:
                    dp[m-1][j1][j2] = grid[m-1][j1]  # Same cell, only count once
                else:
                    dp[m-1][j1][j2] = grid[m-1][j1] + grid[m-1][j2]  # Different cells, add both
        
        # Fill the dp table from the second last row to the top
        for i in range(m-2, -1, -1):
            for j1 in range(n):
                for j2 in range(n):
                    max_chocolates = float('-inf')
                    # Try all possible moves for both robots
                    for dj1 in range(-1, 2):  # Robot 1 moves: -1, 0, 1
                        for dj2 in range(-1, 2):  # Robot 2 moves: -1, 0, 1
                            new_j1 = j1 + dj1
                            new_j2 = j2 + dj2
                            if 0 <= new_j1 < n and 0 <= new_j2 < n:  # Check bounds
                                # Chocolates collected at the current position
                                if j1 == j2:
                                    chocolates = grid[i][j1]  # Both robots at the same cell
                                else:
                                    chocolates = grid[i][j1] + grid[i][j2]  # Different cells
                                
                                # Add the best move from the next row
                                chocolates += dp[i + 1][new_j1][new_j2]
                                
                                # Track the maximum chocolates
                                max_chocolates = max(max_chocolates, chocolates)
                    
                    # Store the maximum chocolates possible for this row
                    dp[i][j1][j2] = max_chocolates
        
        # The result is the max chocolates starting from the top-left and top-right corner
        return dp[0][0][n - 1]


