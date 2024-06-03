'''
136. Single Number
Solved
Easy
Topics
Companies
Hint

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,1]
Output: 1

Example 2:

Input: nums = [4,1,2,1,2]
Output: 4

Example 3:

Input: nums = [1]
Output: 1

'''
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # d=Counter(nums)
        # for k,v in d.items():
        #     if v==1:
        #         return k

        # Approach 2  
        a=0
        for i in nums:
            a^=i
        return a
