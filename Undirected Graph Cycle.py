'''
Given an undirected graph with V vertices labelled from 0 to V-1 and E edges, check whether the graph contains any cycle or not. The Graph is represented as an adjacency list, where adj[i] contains all the vertices that are directly connected to vertex i.

NOTE: The adjacency list represents undirected edges, meaning that if there is an edge between vertex i and vertex j, both j will be adj[i] and i will be in adj[j].

Examples:

Input: adj = [[1], [0,2,4], [1,3], [2,4], [1,3]] 
Output: 1
Explanation: 

1->2->3->4->1 is a cycle.


'''

from typing import List
from collections import deque

class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
		visited=set()
		
		for i in range(V):
		    if i not in visited:
    		    q=deque([(i,-1)])
    		    visited.add(i)
        		while q:
        		    node,parent=q.popleft()
        		    for neigh in adj[node]:
        		        if neigh not in visited:
        		            visited.add(neigh)
        		            q.append((neigh,node))
                    	elif neigh!=parent:
                    	    return True
    		        
    	return False
