'''
3095. Shortest Subarray With OR at Least K I
Solved
Easy
Companies
Hint

You are given an array nums of non-negative integers and an integer k.

An array is called special if the bitwise OR of all of its elements is at least k.

Return the length of the shortest special non-empty
subarray
of nums, or return -1 if no special subarray exists.

 

Example 1:

Input: nums = [1,2,3], k = 2

Output: 1

Explanation:


'''

class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        min_length = n + 1  # Initialize with a value greater than any possible subarray length
        for start in range(n):
            current_or = 0
            for end in range(start, n):
                current_or |= nums[end]
                if current_or >= k:
                    min_length = min(min_length, end - start + 1)
        return min_length if min_length <= n else -1
