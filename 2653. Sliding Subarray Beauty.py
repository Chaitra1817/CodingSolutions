'''
2653. Sliding Subarray Beauty
Solved
Medium
Topics
Companies
Hint

Given an integer array nums containing n integers, find the beauty of each subarray of size k.

The beauty of a subarray is the xth smallest integer in the subarray if it is negative, or 0 if there are fewer than x negative integers.

Return an integer array containing n - k + 1 integers, which denote the beauty of the subarrays in order from the first index in the array.

    A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,-1,-3,-2,3], k = 3, x = 2
Output: [-1,-2,-2]
Explanation: There are 3 subarrays with size k = 3. 
The first subarray is [1, -1, -3] and the 2nd smallest negative integer is -1. 
The second subarray is [-1, -3, -2] and the 2nd smallest negative integer is -2. 
The third subarray is [-3, -2, 3] and the 2nd smallest negative integer is -2.

Example 2:

Input: nums = [-1,-2,-3,-4,-5], k = 2, x = 2
Output: [-1,-2,-3,-4]
Explanation: There are 4 subarrays with size k = 2.
For [-1, -2], the 2nd smallest negative integer is -1.
For [-2, -3], the 2nd smallest negative integer is -2.
For [-3, -4], the 2nd smallest negative integer is -3.
For [-4, -5], the 2nd smallest negative integer is -4. 

'''

from sortedcontainers import SortedList
from typing import List

class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        l, r = 0, 0 
        sorted_window = SortedList()  
        ans = []  

        while r < len(nums):
            sorted_window.add(nums[r])
            
            if r - l + 1 == k:
                if x <= len(sorted_window) and sorted_window[x-1] < 0:
                    ans.append(sorted_window[x-1])
                else:
                    ans.append(0)
                sorted_window.remove(nums[l])
                l += 1

            r += 1

        return ans

'''
In this code, SortedList from the sortedcontainers library is used to maintain a sorted order efficiently. 
The add and remove operations on SortedList have time complexity of O(logk), 
where k is the number of elements in the sorted list. 
This improves the overall time complexity of the solution.
'''
