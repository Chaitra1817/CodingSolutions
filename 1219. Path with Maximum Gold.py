'''
In a gold mine grid of size m x n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.

Return the maximum amount of gold you can collect under the conditions:

    Every time you are located in a cell you will collect all the gold in that cell.
    From your position, you can walk one step to the left, right, up, or down.
    You can't visit the same cell more than once.
    Never visit a cell with 0 gold.
    You can start and stop collecting gold from any position in the grid that has some gold.

 

Example 1:

Input: grid = [[0,6,0],[5,8,7],[0,9,0]]
Output: 24
Explanation:
[[0,6,0],
 [5,8,7],
 [0,9,0]]
Path to get the maximum gold, 9 -> 8 -> 7.

'''

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited=[[0]*n for i in range(m)]

        dir = [(0,1), (1,0), (0,-1), (-1,0)]
        def find(i,j):
            visited[i][j]=1
            cur=0
            for r,c in dir:
                nr, nc = i + r, j + c
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] != 0 and visited[nr][nc]==0:
                    cur=max(cur,find(nr,nc))
            visited[i][j]=0
            return cur+grid[i][j]

        mx=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]!=0:
                    mx=max(mx,find(i,j))
        return mx
