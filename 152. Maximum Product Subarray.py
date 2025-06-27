'''
Given an integer array nums, find a

that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

 

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

 

Constraints:

    1 <= nums.length <= 2 * 104
    -10 <= nums[i] <= 10
    The product of any subarray of nums is guaranteed to fit in a 32-bit integer.
'''

'''
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mx=-1
        for i in range(len(nums)-1):
            prod=1
            for j in range(i,len(nums)):
                mx=max(mx,prod*nums[j])
        return mx

'''
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0

        ans=nums[0]
        mx_so_far=nums[0]
        mn_so_far=nums[0]
        
        for num in nums[1:]:
            temp_mx=mx_so_far
            mx_so_far=max(num, max(mx_so_far*num, mn_so_far*num))
            mn_so_far=min(num, min(temp_mx*num, mn_so_far*num))
            ans=max(ans,mx_so_far)

        return ans
