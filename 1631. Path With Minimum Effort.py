'''
1631. Path With Minimum Effort
Solved
Medium
Topics
Companies
Hint

You are a hiker preparing for an upcoming hike. You are given heights, a 2D array of size rows x columns, where heights[row][col] represents the height of cell (row, col). You are situated in the top-left cell, (0, 0), and you hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can move up, down, left, or right, and you wish to find a route that requires the minimum effort.

A route's effort is the maximum absolute difference in heights between two consecutive cells of the route.

Return the minimum effort required to travel from the top-left cell to the bottom-right cell.

 

Example 1:

Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
Output: 2
Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
This is better than the route of [1,2,2,2,5], where the maximum absolute difference is 3.


'''

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        import heapq
        
        # Priority queue to manage which cell to visit next based on the minimum effort required so far.
        min_heap = [(0, 0, 0)]  # effort, row, column
        visited = [[False] * n for _ in range(m)]
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
        while min_heap:
            effort, x, y = heapq.heappop(min_heap)
            
            if x == m - 1 and y == n - 1:
                return effort
            
            if visited[x][y]:
                continue
            visited[x][y] = True
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    # Calculate the effort to the next cell as the max of current path effort and the height difference
                    next_effort = max(effort, abs(heights[nx][ny] - heights[x][y]))
                    heapq.heappush(min_heap, (next_effort, nx, ny))
        
        return 0
