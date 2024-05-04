'''
494. Target Sum
Solved
Medium
Topics
Companies

You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

    For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".

Return the number of different expressions that you can build, which evaluates to target.

 

Example 1:

Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3

Example 2:

Input: nums = [1], target = 1
Output: 1

'''

from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n=len(nums)
        memo={}
        def find(idx, total):
            if idx == n:
                if total == target:
                    return 1
                else:
                    return 0
            if (idx,total) in memo:
                return memo[(idx,total)]
                    
            positive = find(idx + 1, total + nums[idx])
            negative = find(idx + 1, total - nums[idx])

           
            memo[(idx,total)] = positive + negative
            return memo[(idx,total)]
        
        return find(0, 0)
     
     
