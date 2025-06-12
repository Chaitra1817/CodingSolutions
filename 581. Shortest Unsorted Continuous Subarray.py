'''
Given an integer array nums, you need to find one continuous subarray such that if you only sort this subarray in non-decreasing order, then the whole array will be sorted in non-decreasing order.

Return the shortest such subarray and output its length.

 

Example 1:

Input: nums = [2,6,4,8,10,9,15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.

Example 2:

Input: nums = [1,2,3,4]
Output: 0

Example 3:

Input: nums = [1]
Output: 0

 '''

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n=len(nums)
        if n==0:
            return 0

        i,j=0,n-1

        while i+1<=n-1 and nums[i]<=nums[i+1]:
            i+=1
        
        if i==n-1:
            return 0
        
        while j-1>=0 and nums[j]>=nums[j-1]:
            j-=1
        
        mn=min(nums[i:j+1])
        mx=max(nums[i:j+1])

        while i>0 and nums[i-1]>mn:
            i-=1
        
        while j<n-1 and nums[j+1]<mx:
            j+=1

        return j-i+1
       
