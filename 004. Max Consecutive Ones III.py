'''
004. Max Consecutive Ones III
Solved
Medium
Topics
Companies
Hint

Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

'''
from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l, r = 0, 0
        max_length = 0
        remaining_flips = k
        n = len(nums)

        while r < n:
            if nums[r] == 1:
                r += 1
            elif nums[r] == 0 and remaining_flips > 0:
                r += 1
                remaining_flips -= 1
            else:
                if nums[l] == 0:
                    remaining_flips += 1
                l += 1

            max_length = max(max_length, r - l)

        return max_length
