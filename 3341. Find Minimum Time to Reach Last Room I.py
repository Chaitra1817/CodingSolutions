'''
There is a dungeon with n x m rooms arranged as a grid.

You are given a 2D array moveTime of size n x m, where moveTime[i][j] represents the minimum time in seconds when you can start moving to that room. You start from the room (0, 0) at time t = 0 and can move to an adjacent room. Moving between adjacent rooms takes exactly one second.

Return the minimum time to reach the room (n - 1, m - 1).

Two rooms are adjacent if they share a common wall, either horizontally or vertically.

 

Example 1:

Input: moveTime = [[0,4],[4,4]]

Output: 6

Explanation:

The minimum time required is 6 seconds.

    At time t == 4, move from room (0, 0) to room (1, 0) in one second.
    At time t == 5, move from room (1, 0) to room (1, 1) in one second.

Example 2:

Input: moveTime = [[0,0,0],[0,0,0]]

Output: 3

Explanation:

The minimum time required is 3 seconds.

    At time t == 0, move from room (0, 0) to room (1, 0) in one second.
    At time t == 1, move from room (1, 0) to room (1, 1) in one second.
    At time t == 2, move from room (1, 1) to room (1, 2) in one second.


'''

import sys
import heapq
from typing import List

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        m, n = len(moveTime), len(moveTime[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # Down, Right, Up, Left
        visited = {}
        
        # Priority queue to store (time, x, y) tuples
        pq = [(0, 0, 0)]  # Start at (0,0) with time 0

        while pq:
            t, i, j = heapq.heappop(pq)

            # If we've reached the bottom-right cell, return the time taken
            if i == m - 1 and j == n - 1:
                return t
            
            # If already visited with a lower time, skip this cell
            if (i, j) in visited and visited[(i, j)] <= t:
                continue
            visited[(i, j)] = t

            # Explore neighbors
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n:
                    # Calculate the wait tiwait_timeme if current time < moveTime[ni][nj]
                    wait_time = max(t, moveTime[ni][nj]) + 1
                    heapq.heappush(pq, (wait_time, ni, nj))
        
        return -1  # If no path is found (shouldn't happen with valid input)
