'''
743. Network Delay Time
Solved
Medium
Topics
Companies
Hint

You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

 

Example 1:

Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2

Example 2:

Input: times = [[1,2,1]], n = 2, k = 1
Output: 1


'''

from heapq import heappop, heappush
import collections

class Solution:
    def networkDelayTime(self, times, n, k):
        graph = collections.defaultdict(list)
        # Create the graph
        for u, v, w in times:
            graph[u].append((v, w))

        # Min-heap priority queue
        min_heap = [(0, k)]  # (distance, node)
        # Distances array
        distances = {node: float('inf') for node in range(1, n + 1)}
        distances[k] = 0

        while min_heap:
            cur_dist, u = heappop(min_heap)

            if cur_dist > distances[u]:
                continue

            # Process each adjacent node v
            for v, weight in graph[u]:
                dist = cur_dist + weight
                # Only consider this new path if it's better
                if dist < distances[v]:
                    distances[v] = dist
                    heappush(min_heap, (dist, v))

        # The answer is the maximum distance to any node
        max_dist = max(distances.values())
        return max_dist if max_dist < float('inf') else -1
