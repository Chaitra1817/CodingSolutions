'''
Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

 

Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.

Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.

'''

import math
import sys

class Solution:
    def numSquares(self, n: int) -> int:
        memo = {}

        def dfs(remaining):
            # Base case: when remaining is 0, no more numbers are needed.
            if remaining == 0:
                return 0
            
            # If the result for this remaining value is already computed, return it.
            if remaining in memo:
                return memo[remaining]
            
            # Initialize minimum count to a large number.
            min_count = sys.maxsize
            
            # Try every possible perfect square number that is less than or equal to 'remaining'
            i = 1
            while i * i <= remaining:
                min_count = min(min_count, 1 + dfs(remaining - i * i))
                i += 1
            
            # Memoize and return the minimum count for this remaining value.
            memo[remaining] = min_count
            return memo[remaining]

        return dfs(n)
