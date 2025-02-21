'''
Given a weighted, undirected and connected graph where you have given adjacency list adj. You have to find the shortest distance of all the vertices from the source vertex src, and return a list of integers denoting the shortest distance between each node and source vertex src.

Note: The Graph doesn't contain any negative weight edge.

Examples:

Input: adj = [[[1, 9]], [[0, 9]]], src = 0
Output: [0, 9]
Explanation:

The source vertex is 0. Hence, the shortest distance of node 0 is 0 and the shortest distance from node 0 to 1 is 9.

'''

import heapq
from typing import List, Tuple

def dijkstra(adj: List[List[Tuple[int, int]]], src: int) -> List[int]:
    n = len(adj)
    ans = [float('inf')] * n
    ans[src] = 0  # Distance to source is 0
    pq = [(0, src)]  # Min-heap (priority queue) initialized with (distance, node)
    
    while pq:
        dist, node = heapq.heappop(pq)  # Extract node with the smallest distance
        
        if dist > ans[node]:  # Skip outdated entries
            continue
        
        for neighbor, weight in adj[node]:  # Loop over neighbors
            new_dist = dist + weight
            if new_dist < ans[neighbor]:  # Found a shorter path
                ans[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))  # Push updated distance
            
    return ans
