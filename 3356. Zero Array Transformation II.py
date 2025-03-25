'''

3356. Zero Array Transformation II
Solved
Medium
Topics
Companies
Hint

You are given an integer array nums of length n and a 2D array queries where queries[i] = [li, ri, vali].

Each queries[i] represents the following action on nums:

    Decrement the value at each index in the range [li, ri] in nums by at most vali.
    The amount by which each value is decremented can be chosen independently for each index.

A Zero Array is an array with all its elements equal to 0.

Return the minimum possible non-negative value of k, such that after processing the first k queries in sequence, nums becomes a Zero Array. If no such k exists, return -1.

 

Example 1:

Input: nums = [2,0,2], queries = [[0,2,1],[0,2,1],[1,1,3]]

Output: 2

Explanation:

    For i = 0 (l = 0, r = 2, val = 1):
        Decrement values at indices [0, 1, 2] by [1, 0, 1] respectively.
        The array will become [1, 0, 1].
    For i = 1 (l = 0, r = 2, val = 1):
        Decrement values at indices [0, 1, 2] by [1, 0, 1] respectively.
        The array will become [0, 0, 0], which is a Zero Array. Therefore, the minimum value of k is 2.

'''

from typing import List

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        def can_make_zero(k: int) -> bool:
            n = len(nums)
            diff = [0] * (n + 1)  
            for i in range(k):
                l, r, v = queries[i]
                diff[l] += v
                if r + 1 < len(diff):
                    diff[r + 1] -= v

            total = 0
            for i in range(n):
                total += diff[i]
                if total < nums[i]:
                    return False
            return True

        left, right = 0, len(queries)
        answer = -1

        while left <= right:
            mid = (left + right) // 2
            if can_make_zero(mid):
                answer = mid
                right = mid - 1  
            else:
                left = mid + 1

        return answer

