'''
Given an undirected graph with V vertices. We say two vertices u and v belong to a single province if there is a path from u to v or v to u. Your task is to find the number of provinces.

Note: A province is a group of directly or indirectly connected cities and no other cities outside of the group.

Example 1:

Input:
[
 [1, 0, 1],
 [0, 1, 0],
 [1, 0, 1]
]

Output:
2
'''
from collections import deque

class Solution:
    def numProvinces(self, adj, V):
        # Convert adjacency matrix to adjacency list
        graph = {}
        for i in range(V):
            graph[i] = []  # Initialize each node with an empty list

        for i in range(V):
            for j in range(V):
                if adj[i][j] == 1 and i != j:
                    graph[i].append(j)

        q = deque()
        visited = set()
        provinces = 0

        for i in range(V):
            if i not in visited:
                q.append(i)
                provinces += 1
                
                while q:
                    node = q.popleft()
                    if node not in visited:
                        visited.add(node)
                        for neigh in graph[node]:
                            if neigh not in visited:
                                q.append(neigh)
        
        return provinces
