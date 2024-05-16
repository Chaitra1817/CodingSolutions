'''
1976. Number of Ways to Arrive at Destination
Solved
Medium
Topics
Companies
Hint

You are in a city that consists of n intersections numbered from 0 to n - 1 with bi-directional roads between some intersections. The inputs are generated such that you can reach any intersection from any other intersection and that there is at most one road between any two intersections.

You are given an integer n and a 2D integer array roads where roads[i] = [ui, vi, timei] means that there is a road between intersections ui and vi that takes timei minutes to travel. You want to know in how many ways you can travel from intersection 0 to intersection n - 1 in the shortest amount of time.

Return the number of ways you can arrive at your destination in the shortest amount of time. Since the answer may be large, return it modulo 109 + 7.

 

Example 1:

Input: n = 7, roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
Output: 4
Explanation: The shortest amount of time it takes to go from intersection 0 to intersection 6 is 7 minutes.
The four ways to get there in 7 minutes are:
- 0 ➝ 6
- 0 ➝ 4 ➝ 6
- 0 ➝ 1 ➝ 2 ➝ 5 ➝ 6
- 0 ➝ 1 ➝ 3 ➝ 5 ➝ 6

'''

from heapq import heappush, heappop
from collections import defaultdict
import sys

class Solution:
    def countPaths(self,n, roads):
        MOD = 10**9 + 7
        adj = defaultdict(list)
        for u, v, w in roads:
            adj[u].append((v, w))
            adj[v].append((u, w))
        
        pq = [(0, 0)]  # (current weight, node)
        dist = [sys.maxsize] * n
        dist[0] = 0
        path_count = [0] * n
        path_count[0] = 1  # Initial path count for starting point

        while pq:
            current_weight, node = heappop(pq)

            if current_weight > dist[node]:
                continue

            for next_node, weight in adj[node]:
                new_weight = current_weight + weight

                if new_weight < dist[next_node]:
                    dist[next_node] = new_weight
                    path_count[next_node] = path_count[node]
                    heappush(pq, (new_weight, next_node))
                elif new_weight == dist[next_node]:
                    path_count[next_node] = (path_count[next_node] + path_count[node]) % MOD

        return path_count[n-1] if dist[n-1] != sys.maxsize else 0

# TLE
    # def countPaths(self,n, roads):
    #     MOD = 10**9 + 7
    #     adj = defaultdict(list)
    #     for u, v, w in roads:
    #         adj[u].append((v, w))
    #         adj[v].append((u, w))
        
    #     pq = [(0, 0)]  # (current travel time, node)
    #     dist = [sys.maxsize] * n
    #     dist[0] = 0
    #     min_paths = defaultdict(int)

    #     while pq:
    #         current_time, node = heappop(pq)

    #         if node == n-1:
    #             min_paths[current_time] += 1

    #         if current_time > dist[node]:
    #             continue

    #         for next_node, time in adj[node]:
    #             new_time = current_time + time

    #             if new_time < dist[next_node]:
    #                 dist[next_node] = new_time
    #                 heappush(pq, (new_time, next_node))
    #             elif new_time == dist[next_node]:
    #                 heappush(pq, (new_time, next_node))

    #     # Finding the minimum time and its count
    #     if min_paths:
    #         min_time = min(min_paths.keys())
    #         return min_paths[min_time] % MOD
    #     return 0
