'''
4. Median of Two Sorted Arrays
Solved
Hard
Topics
Companies

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

 

Constraints:

    nums1.length == m
    nums2.length == n
    0 <= m <= 1000
    0 <= n <= 1000
    1 <= m + n <= 2000
    -106 <= nums1[i], nums2[i] <= 106


'''

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = len(nums1), len(nums2)
        idx1, idx2 = -1, -1

        if (n1 + n2) % 2 == 0:
            idx1 = (n1 + n2) // 2 - 1
            idx2 = (n1 + n2) // 2
        else:
            idx1 = (n1 + n2) // 2

        cur = 0  # Current index in the merged array
        i, j = 0, 0
        first, second = 0, 0

        while i < n1 or j < n2:
            if i < n1 and (j >= n2 or nums1[i] <= nums2[j]):
                if cur == idx1:
                    first = nums1[i]
                if cur == idx2:
                    second = nums1[i]
                i += 1
            else:
                if cur == idx1:
                    first = nums2[j]
                if cur == idx2:
                    second = nums2[j]
                j += 1

            cur += 1

            if (n1 + n2) % 2 != 0 and cur > idx1:
                return first

        if (n1 + n2) % 2 == 0:
            return (first + second) / 2.0
