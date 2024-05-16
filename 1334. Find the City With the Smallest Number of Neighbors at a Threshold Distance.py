'''
1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance
Solved
Medium
Topics
Companies
Hint

There are n cities numbered from 0 to n-1. Given the array edges where edges[i] = [fromi, toi, weighti] represents a bidirectional and weighted edge between cities fromi and toi, and given the integer distanceThreshold.

Return the city with the smallest number of cities that are reachable through some path and whose distance is at most distanceThreshold, If there are multiple such cities, return the city with the greatest number.

Notice that the distance of a path connecting cities i and j is equal to the sum of the edges' weights along that path.

 

Example 1:

Input: n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4
Output: 3
Explanation: The figure above describes the graph. 
The neighboring cities at a distanceThreshold = 4 for each city are:
City 0 -> [City 1, City 2] 
City 1 -> [City 0, City 2, City 3] 
City 2 -> [City 0, City 1, City 3] 
City 3 -> [City 1, City 2] 
Cities 0 and 3 have 2 neighboring cities at a distanceThreshold = 4, but we have to return city 3 since it has the greatest number.

'''

from collections import defaultdict
import heapq

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adj = defaultdict(list)
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))

        ans = -1
        min_count = n

        for i in range(n):
            dist = [float('inf')] * n
            dist[i] = 0
            pq = [(0, i)]

            while pq:
                d, node = heapq.heappop(pq)
                if d > distanceThreshold:
                    break
                for neighbor, weight in adj[node]:
                    if dist[node] + weight < dist[neighbor]:
                        dist[neighbor] = dist[node] + weight
                        heapq.heappush(pq, (dist[neighbor], neighbor))

            count = sum(dist[node] <= distanceThreshold for node in range(n))
            if count <= min_count:
                min_count = count
                ans = i

        return ans
