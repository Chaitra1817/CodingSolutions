'''
Given a Directed Graph with V vertices (Numbered from 0 to V-1) and E edges, check whether it contains any cycle or not.
The graph is represented as an adjacency list, where adj[i] contains a list of vertices that are directly reachable from vertex i. Specifically, adj[i][j] represents an edge from vertex i to vertex j.

Example 1:

Input:



Output: 1
Explanation: 3 -> 3 is a cycle

'''

#User function Template for python3
from typing import List
from collections import deque

class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, adj : List[List[int]]) -> bool :
        in_degree = [0] * V  # In-degree array
        
        # Step 1: Compute in-degree of each node
        for node in range(V):
            for neighbor in adj[node]:
                in_degree[neighbor] += 1

        # Step 2: Push all nodes with in-degree 0 into the queue
        queue = deque()
        for i in range(V):
            if in_degree[i] == 0:
                queue.append(i)

        # Step 3: Process nodes in topological order
        count = 0  # Count of processed nodes
        while queue:
            node = queue.popleft()
            count += 1  # Processed one more node
            
            # Reduce in-degree of all adjacent nodes
            for neighbor in adj[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # Step 4: If count != V, then a cycle exists
        return count != V
        
