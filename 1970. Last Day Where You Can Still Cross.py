'''
There is a 1-based binary matrix where 0 represents land and 1 represents water. You are given integers row and col representing the number of rows and columns in the matrix, respectively.

Initially on day 0, the entire matrix is land. However, each day a new cell becomes flooded with water. You are given a 1-based 2D array cells, where cells[i] = [ri, ci] represents that on the ith day, the cell on the rith row and cith column (1-based coordinates) will be covered with water (i.e., changed to 1).

You want to find the last day that it is possible to walk from the top to the bottom by only walking on land cells. You can start from any cell in the top row and end at any cell in the bottom row. You can only travel in the four cardinal directions (left, right, up, and down).

Return the last day where it is possible to walk from the top to the bottom by only walking on land cells.

 

Example 1:

Input: row = 2, col = 2, cells = [[1,1],[2,1],[1,2],[2,2]]
Output: 2
Explanation: The above image depicts how the matrix changes each day starting from day 0.
The last day where it is possible to cross from top to bottom is on day 2.

Example 2:

Input: row = 2, col = 2, cells = [[1,1],[1,2],[2,1],[2,2]]
Output: 1
Explanation: The above image depicts how the matrix changes each day starting from day 0.
The last day where it is possible to cross from top to bottom is on day 1.

Example 3:

Input: row = 3, col = 3, cells = [[1,2],[2,1],[3,3],[2,2],[1,1],[1,3],[2,3],[3,2],[3,1]]
Output: 3
Explanation: The above image depicts how the matrix changes each day starting from day 0.
The last day where it is possible to cross from top to bottom is on day 3.

 

Constraints:

    2 <= row, col <= 2 * 104
    4 <= row * col <= 2 * 104
    cells.length == row * col
    1 <= ri <= row
    1 <= ci <= col
    All the values of cells are unique.

'''

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        
        def cancross(day):
            matrix=[[0]*col for r in range(row)]
            q=deque([])
            
            for d in range(day):
                calcr,calcc=cells[d][0]-1,cells[d][1]-1
                matrix[calcr][calcc]=1
            
            for c in range(col):
                if matrix[0][c]==0:                                                                                                                                                                
                    q.append((0,c))
                    matrix[0][c]=2

            directions=[(-1,0),(0,1),(1,0),(0,-1)]
            while q:
                r,c=q.popleft()
                if r==row-1:
                    return True

                for dr,dc in directions:
                    nr,nc=r+dr,c+dc
                    if nr>=0 and nc>=0 and nr<=row-1 and nc<=col-1 and matrix[nr][nc]==0:
                        matrix[nr][nc]=2
                        q.append((nr,nc))

            return False


        ans=0
        low,high=1,len(cells)
        while low<=high:
            mid=(low+high)//2
            if cancross(mid):
                ans=mid
                low=mid+1
            else:
                high=mid-1
        return ans

        
