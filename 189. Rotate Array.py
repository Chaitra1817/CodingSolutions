'''
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

 

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

 

Constraints:

    1 <= nums.length <= 105
    -231 <= nums[i] <= 231 - 1
    0 <= k <= 105

 

Follow up:

    Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
    Could you do it in-place with O(1) extra space?

'''

'''
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n=len(nums)
        temp=[0]*n
        for i in range(len(nums)):
            idx=(i+k)%n
            temp[idx]=nums[i]

        for i in range(n):
            nums[i]=temp[i]
'''

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums)
        start,cnt=0,0
        while cnt<n:
            cur,prev=start,nums[start]
            while True:
                nxt_idx=(cur+k)%n
                nums[nxt_idx],prev=prev,nums[nxt_idx]
                cur=nxt_idx
                cnt+=1
                if start==cur:
                    break
            start+=1
