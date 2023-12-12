'''
213. House Robber II
Solved
Medium
Topics
Companies
Hint

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

Example 2:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 3:

Input: nums = [1,2,3]
Output: 3

'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<=3:
            return max(nums)
        def maximumNonAdjacentSum(arr): 
            prev=arr[0]
            prev2=0
            n=len(arr)
            for i in range(1,n):
                if i==0:
                    return arr[i]
                if i<0:
                    return 0
                
                take=arr[i]
                if i>1:
                    take+=prev2
                notTake=prev

                cur=max(take,notTake)
                prev2=prev
                prev=cur

            return prev
        
        return max(maximumNonAdjacentSum(nums[:-1]),maximumNonAdjacentSum(nums[1:]))
