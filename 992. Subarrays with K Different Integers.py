'''
992. Subarrays with K Different Integers
Solved
Hard
Topics
Companies

Given an integer array nums and an integer k, return the number of good subarrays of nums.

A good array is an array where the number of different integers in that array is exactly k.

    For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [1,2,1,2,3], k = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]

Example 2:

Input: nums = [1,2,1,3,4], k = 3
Output: 3
Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].


'''

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def find(nums, k):
            l, r = 0, 0
            cnt = 0
            d = {}
            n = len(nums)

            while r < n:
                d[nums[r]] = d.get(nums[r], 0) + 1
                while len(d) > k:
                    d[nums[l]] -= 1
                    if d[nums[l]] == 0:
                        del d[nums[l]]
                    l += 1
                cnt += r - l + 1
                r += 1
            
            return cnt
        
        return find(nums, k) - find(nums, k - 1)
