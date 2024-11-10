'''
There is a dungeon with n x m rooms arranged as a grid.

You are given a 2D array moveTime of size n x m, where moveTime[i][j] represents the minimum time in seconds when you can start moving to that room. You start from the room (0, 0) at time t = 0 and can move to an adjacent room. Moving between adjacent rooms takes one second for one move and two seconds for the next, alternating between the two.

Return the minimum time to reach the room (n - 1, m - 1).

Two rooms are adjacent if they share a common wall, either horizontally or vertically.

 

Example 1:

Input: moveTime = [[0,4],[4,4]]

Output: 7

Explanation:

The minimum time required is 7 seconds.

    At time t == 4, move from room (0, 0) to room (1, 0) in one second.
    At time t == 5, move from room (1, 0) to room (1, 1) in two seconds.

Example 2:

Input: moveTime = [[0,0,0,0],[0,0,0,0]]

Output: 6

Explanation:

The minimum time required is 6 seconds.

    At time t == 0, move from room (0, 0) to room (1, 0) in one second.
    At time t == 1, move from room (1, 0) to room (1, 1) in two seconds.
    At time t == 3, move from room (1, 1) to room (1, 2) in one second.
    At time t == 4, move from room (1, 2) to room (1, 3) in two seconds.

'''

import heapq
from typing import List

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        m, n = len(moveTime), len(moveTime[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # Down, Right, Up, Left
        visited = {}
        
        # Priority queue to store (time, moves, x, y) tuples
        pq = [(0, 0, 0, 1)]  # Start at (0,0) with time 0 and move count 1

        while pq:
            t, i, j,moves = heapq.heappop(pq)

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
                    # Calculate the time to enter the next cell
                    next_time = max(t, moveTime[ni][nj]) + moves
                    if moves==1:
                        nMoves=2
                    else:
                        nMoves=1
                    heapq.heappush(pq, (next_time, ni, nj,nMoves))
        
        return -1  # If no path is found (shouldn't happen with valid input)
