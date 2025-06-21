'''

An n x n grid is composed of 1 x 1 squares where each 1 x 1 square consists of a '/', '\', or blank space ' '. These characters divide the square into contiguous regions.

Given the grid grid represented as a string array, return the number of regions.

Note that backslash characters are escaped, so a '\' is represented as '\\'.

 

Example 1:

Input: grid = [" /","/ "]
Output: 2

Example 2:

Input: grid = [" /","  "]
Output: 1

Example 3:

Input: grid = ["/\\","\\/"]
Output: 5
Explanation: Recall that because \ characters are escaped, "\\/" refers to \/, and "/\\" refers to /\.

 

Constraints:

    n == grid.length == grid[i].length
    1 <= n <= 30
    grid[i][j] is either '/', '\', or ' '.

'''

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        m,n=len(grid),len(grid[0])
        m2,n2=m*3,n*3
        grid2=[[0 for j in range(n2+1)]for i in range(m2+1)]

        for i in range(m):
            for j in range(n):
                nr,nc=i*3,j*3
                if grid[i][j]=="/":
                    grid2[nr][nc+2]=1
                    grid2[nr+1][nc+1]=1
                    grid2[nr+2][nc]=1
                elif grid[i][j]=="\\":
                    grid2[nr][nc]=1
                    grid2[nr+1][nc+1]=1
                    grid2[nr+2][nc+2]=1
        
        def isValid(r,c):
            return r>=0 and r<=m2-1 and c>=0 and c<=n2-1

        def dfs(i,j):
             visited.add((i,j))
             directions=[(-1,0),(0,1),(1,0),(0,-1)]
             for dr,dc in directions:
                nr,nc=i+dr,j+dc
                if isValid(nr,nc):
                    if (nr,nc) not in visited and grid2[nr][nc]==0:
                        dfs(nr,nc)
        
        ans=0
        visited=set()
        for i in range(m2):
            for j in range(n2):
                if grid2[i][j]==0 and (i,j) not in visited:
                    dfs(i,j)
                    ans+=1
        return ans
