'''
2812. Find the Safest Path in a Grid
Solved
Medium
Topics
Companies
Hint

You are given a 0-indexed 2D matrix grid of size n x n, where (r, c) represents:

    A cell containing a thief if grid[r][c] = 1
    An empty cell if grid[r][c] = 0

You are initially positioned at cell (0, 0). In one move, you can move to any adjacent cell in the grid, including cells containing thieves.

The safeness factor of a path on the grid is defined as the minimum manhattan distance from any cell in the path to any thief in the grid.

Return the maximum safeness factor of all paths leading to cell (n - 1, n - 1).

An adjacent cell of cell (r, c), is one of the cells (r, c + 1), (r, c - 1), (r + 1, c) and (r - 1, c) if it exists.

The Manhattan distance between two cells (a, b) and (x, y) is equal to |a - x| + |b - y|, where |val| denotes the absolute value of val.

Input: grid = [[0,0,1],[0,0,0],[0,0,0]]
Output: 2
Explanation: The path depicted in the picture above has a safeness factor of 2 since:
- The closest cell of the path to the thief at cell (0, 2) is cell (0, 0). The distance between them is | 0 - 0 | + | 0 - 2 | = 2.
It can be shown that there are no other paths with a higher safeness factor.

'''

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n=len(grid)

        mndist={}
        directions=[(-1,0),(0,1),(1,0),(0,-1)]
        def preComputeDistanceFromThief():
            q=deque()
            
            for i in range(n):
                for j in range(n):
                    if grid[i][j]==1:
                        mndist[(i,j)]=0
                        q.append((i,j,0))
            
            while q:
                r,c,d=q.popleft()
                for dr,dc in directions:
                    nr,nc=r+dr,c+dc
                    if nr>=0 and nr<=n-1 and nc>=0 and nc<=n-1:
                        if (nr,nc) not in mndist:
                            mndist[nr,nc]=d+1
                            q.append((nr,nc,d+1))

        preComputeDistanceFromThief()

        mheap=[]
        heapq.heappush(mheap,(-mndist[0,0],0,0))
        visited=set()
        visited.add((0,0))
        while mheap:
            d,r,c= heapq.heappop(mheap)
            d=-d
            if r==n-1 and c==n-1:
                return d

            for dr,dc in directions:
                nr,nc=r+dr,c+dc
                if nr>=0 and nr<=n-1 and nc>=0 and nc<=n-1:
                    if (nr,nc) not in visited:
                        visited.add((nr,nc))
                        sofarmn=min(mndist[(nr,nc)],d)
                        heapq.heappush(mheap,(-sofarmn,nr,nc))
        return -1
            

# TC: O(n**2 logn)
# SC: O(n**2)
