
'''

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

 

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2

Example 2:

Input: nums = [3,1,3,4,2]
Output: 3

Example 3:

Input: nums = [3,3,3,3,3]
Output: 3

'''

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d=Counter(nums)
        mx=max(d.values())
        for k,v in d.items():
            if v==mx:
                return k
        
