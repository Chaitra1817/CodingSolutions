'''
You are given a rows x cols matrix grid representing a field of cherries where grid[i][j] represents the number of cherries that you can collect from the (i, j) cell.

You have two robots that can collect cherries for you:

    Robot #1 is located at the top-left corner (0, 0), and
    Robot #2 is located at the top-right corner (0, cols - 1).

Return the maximum number of cherries collection using both robots by following the rules below:

    From a cell (i, j), robots can move to cell (i + 1, j - 1), (i + 1, j), or (i + 1, j + 1).
    When any robot passes through a cell, It picks up all cherries, and the cell becomes an empty cell.
    When both robots stay in the same cell, only one takes the cherries.
    Both robots cannot move outside of the grid at any moment.
    Both robots should reach the bottom row in grid.

Input: grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]
Output: 24
Explanation: Path of robot #1 and #2 are described in color green and blue respectively.
Cherries taken by Robot #1, (3 + 2 + 5 + 2) = 12.
Cherries taken by Robot #2, (1 + 5 + 5 + 1) = 12.
Total of cherries: 12 + 12 = 24.

'''

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])

        @cache
        def find(i,j1,j2):
            nonlocal m,n,grid
            if j1 < 0 or j1 >= n or j2 < 0 or j2 >= n:
                return float('-inf')
            if i==m-1:
                if j1==j2:
                    return grid[i][j1]
                else:
                    return grid[i][j1]+grid[i][j2]

            maxi=-1e8
            for dj1 in range(-1,2):
                for dj2 in range(-1,2):
                    val=0
                    if j1==j2:
                        val=grid[i][j1]
                    else:
                        val=grid[i][j1]+grid[i][j2]
                        val+=find(i+1,j1+dj1,j2+dj2)
                    maxi=max(maxi,val)
            return maxi
        
        return find(0,0,n-1)
