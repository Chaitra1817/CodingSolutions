'''
You are given an integer array nums.

Return the smallest index i such that the sum of the digits of nums[i] is equal to i.

If no such index exists, return -1.

 

Example 1:

Input: nums = [1,3,2]

Output: 2

Explanation:

    For nums[2] = 2, the sum of digits is 2, which is equal to index i = 2. Thus, the output is 2.

Example 2:

Input: nums = [1,10,11]

Output: 1

Explanation:

    For nums[1] = 10, the sum of digits is 1 + 0 = 1, which is equal to index i = 1.
    For nums[2] = 11, the sum of digits is 1 + 1 = 2, which is equal to index i = 2.
    Since index 1 is the smallest, the output is 1.


'''

from typing import List

class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            num = nums[i]
            digit_sum = 0
            while num > 0:
                digit_sum += num % 10
                num //= 10

            if digit_sum == i:
                return i
        return -1
