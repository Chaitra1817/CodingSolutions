"""
797. All Paths From Source to Target
Medium
6.9K
138
company
Bloomberg
company
Amazon
company
Adobe

Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).


Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]
Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.


Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
"""

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        target = len(graph) - 1

        def all_paths_to_target(curr_node):
            if curr_node == target:
                return [[target]]

            results = []
            for next_node in graph[curr_node]:
                for path in all_paths_to_target(next_node):
                    print("path",path)
                    results.append([curr_node] + path)

            return results

        return all_paths_to_target(0)
