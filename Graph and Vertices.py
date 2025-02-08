'''

Given an integer n representing number of vertices. Find out how many undirected graphs (not necessarily connected) can be constructed out of a given n number of vertices.

 

Example 1:

Input: 2
Output: 2

Example 2:

Input: 5
Output: 1024

'''

class Solution:
    def count(self, n):
        return 2 ** (n * (n - 1) // 2)

        
