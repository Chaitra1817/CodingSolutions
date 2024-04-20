'''
416. Partition Equal Subset Sum
Solved
Medium
Topics
Companies

Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.

 

Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.

 

Constraints:

    1 <= nums.length <= 200
    1 <= nums[i] <= 100


'''

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def find(idx,target,dp):
            if idx==0:
                if nums[idx]==target:
                    return True
            if idx<0:
                return False
            
            if dp[idx][target]!=-1:
                return dp[idx][target]

            notTake=find(idx-1,target,dp)
            take=False
            if nums[idx]<=target:
                take=find(idx-1,target-nums[idx],dp)

            dp[idx][target] = notTake or take
            return dp[idx][target]


        total=sum(nums)
        if total%2==0:
            target=total//2
            n=len(nums)
            dp=[[-1 for i in range(target+1)]for i in range(n)]
            return find(n-1,target,dp)
        else:
            return False
        

        
