'''
74. Search a 2D Matrix
Solved
Medium
Topics
Companies

You are given an m x n integer matrix matrix with the following two properties:

    Each row is sorted in non-decreasing order.
    The first integer of each row is greater than the last integer of the previous row.

Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

 

Example 1:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

'''

from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])

        def find(row: List[int], target: int) -> bool:
            low, high = 0, n - 1
            while low <= high:
                mid = (low + high) // 2
                if row[mid] == target:
                    return True
                if target < row[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            return False

        low, high = 0, m - 1
        while low <= high:
            mid = (low + high) // 2
            if matrix[mid][0] <= target <= matrix[mid][n - 1]:
                return find(matrix[mid], target)
            if target < matrix[mid][0]:
                high = mid - 1
            else:
                low = mid + 1
        return False
