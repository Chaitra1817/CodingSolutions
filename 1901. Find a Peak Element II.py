'''
1901. Find a Peak Element II
Solved
Medium
Topics
Companies
Hint

A peak element in a 2D grid is an element that is strictly greater than all of its adjacent neighbors to the left, right, top, and bottom.

Given a 0-indexed m x n matrix mat where no two adjacent cells are equal, find any peak element mat[i][j] and return the length 2 array [i,j].

You may assume that the entire matrix is surrounded by an outer perimeter with the value -1 in each cell.

You must write an algorithm that runs in O(m log(n)) or O(n log(m)) time.

 

Example 1:

Input: mat = [[1,4],[3,2]]
Output: [0,1]
Explanation: Both 3 and 4 are peak elements so [1,0] and [0,1] are both acceptable answers.

Example 2:

Input: mat = [[10,20,15],[21,30,14],[7,16,32]]
Output: [1,1]
Explanation: Both 30 and 32 are peak elements so [1,1] and [2,2] are both acceptable answers.

 

Constraints:

    m == mat.length
    n == mat[i].length
    1 <= m, n <= 500
    1 <= mat[i][j] <= 105
    No two adjacent cells are equal.


'''

from typing import List

class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        def find(mat, m, col):
            maxV = -1
            idx = -1
            for i in range(m):
                if mat[i][col] > maxV:
                    maxV = mat[i][col]
                    idx = i
            return idx
        
        m, n = len(mat), len(mat[0])
        low, high = 0, n - 1
        
        while low <= high:
            mid = (low + high) // 2
            maxR = find(mat, m, mid)
            
            left = mat[maxR][mid - 1] if mid - 1 >= 0 else -1
            right = mat[maxR][mid + 1] if mid + 1 < n else -1
            
            if mat[maxR][mid] > left and mat[maxR][mid] > right:
                return [maxR, mid]
            elif mat[maxR][mid] < left:
                high = mid - 1
            else:
                low = mid + 1
        
        return [-1, -1]
