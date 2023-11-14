'''
You are given a 0-indexed integer array nums. You have to partition the array into one or more contiguous subarrays.

We call a partition of the array valid if each of the obtained subarrays satisfies one of the following conditions:

    The subarray consists of exactly 2, equal elements. For example, the subarray [2,2] is good.
    The subarray consists of exactly 3, equal elements. For example, the subarray [4,4,4] is good.
    The subarray consists of exactly 3 consecutive increasing elements, that is, the difference between adjacent elements is 1. For example, the subarray [3,4,5] is good, but the subarray [1,3,5] is not.

Return true if the array has at least one valid partition. Otherwise, return false.

 

Example 1:

Input: nums = [4,4,4,5,6]
Output: true
Explanation: The array can be partitioned into the subarrays [4,4] and [4,5,6].
This partition is valid, so we return true.

Example 2:

Input: nums = [1,1,1,2]
Output: false
Explanation: There is no valid partition for this array.

'''

# 1 Using @cache

class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n=len(nums)
        i=0
        
        @cache
        def isValid(i):
            if i>=n:
                return True
            if i+1<n and nums[i]==nums[i+1] and isValid(i+2):
                return True
            if i+2<n and nums[i]==nums[i+1]==nums[i+2] and isValid(i+3):
                return True
            if i+2<n and nums[i+1]-nums[i]==1 and nums[i+2]-nums[i+1]==1 and isValid(i+3):
                return True
            return False   
        return isValid(i)

# 2 Using dictionary

class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n=len(nums)
        i=0
        d={}
        def isValid(i):
            if i in d:
                return d[i]
            if i>=n:
                return True
            if i+1<n and nums[i]==nums[i+1] and isValid(i+2):
                d[i]=True
                return True
            if i+2<n and nums[i]==nums[i+1]==nums[i+2] and isValid(i+3):
                d[i]=True
                return True
            if i+2<n and nums[i+1]-nums[i]==1 and nums[i+2]-nums[i+1]==1 and isValid(i+3):
                d[i]=True
                return True
            d[i]=False
            return False   
        return isValid(i)

