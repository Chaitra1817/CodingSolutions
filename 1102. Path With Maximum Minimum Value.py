'''
Given an m x n integer matrix grid, return the maximum score of a path starting at (0, 0) and ending at (m - 1, n - 1) moving in the 4 cardinal directions.

The score of a path is the minimum value in that path.

    For example, the score of the path 8 → 4 → 5 → 9 is 4.

 

Example 1:

Input: grid = [[5,4,5],[1,2,6],[7,4,6]]
Output: 4
Explanation: The path with the maximum score is highlighted in yellow. 

Example 2:

Input: grid = [[2,2,1,2,2,2],[1,2,2,2,1,2]]
Output: 2

Example 3:

Input: grid = [[3,4,6,3,4],[0,2,1,1,7],[8,8,3,2,7],[3,2,4,9,8],[4,1,2,0,0],[4,6,5,4,3]]
Output: 3

 

Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 100
    0 <= grid[i][j] <= 109

'''

class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        d=defaultdict(list)
        m,n=len(grid),len(grid[0])
        q=[]
        heapq.heappush(q,(0,0,0,grid[0][0]))
        visited=set()
        directions=[(-1,0),(0,1),(1,0),(0,-1)]
        visited = set()
        while q:
            w,r,c,cur_min=heapq.heappop(q)
            if r==m-1 and c==n-1:
                return cur_min
            if (r,c) in visited:
                continue
            visited.add((r,c))

            for dr,dc in directions:
                nr,nc=r+dr,c+dc
                if nr>=0 and nr<=m-1 and nc>=0 and nc<=n-1 and (nr,nc) not in visited:
                    next_min = min(cur_min, grid[nr][nc])
                    heapq.heappush(q,(-grid[r][c],nr,nc,next_min))
            






        
        
