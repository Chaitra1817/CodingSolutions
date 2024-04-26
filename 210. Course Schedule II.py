'''
210. Course Schedule II
Solved
Medium
Topics
Companies
Hint

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

    For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].

Example 2:

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].

Example 3:

Input: numCourses = 1, prerequisites = []
Output: [0]

'''

from collections import defaultdict, deque
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Building the graph and calculating indegrees
        adj = defaultdict(list)
        indegree = [0] * numCourses
        for dest, src in prerequisites:
            adj[src].append(dest)  # src -> dest, src is a prerequisite for dest
            indegree[dest] += 1    # dest gets an additional prerequisite

        # Queue for processing nodes with zero indegree
        q = deque([i for i in range(numCourses) if indegree[i] == 0])
        
        # List to store the order of courses
        order = []
        while q:
            node = q.popleft()
            order.append(node)
            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
        
        # Check if we were able to process all courses
        if len(order) == numCourses:
            return order
        else:
            return []  # If not all courses are processed, it means there's a cycle

