'''
You are given two integer arrays of the same length nums1 and nums2. In one operation, you are allowed to swap nums1[i] with nums2[i].

    For example, if nums1 = [1,2,3,8], and nums2 = [5,6,7,4], you can swap the element at i = 3 to obtain nums1 = [1,2,3,4] and nums2 = [5,6,7,8].

Return the minimum number of needed operations to make nums1 and nums2 strictly increasing. The test cases are generated so that the given input always makes it possible.

An array arr is strictly increasing if and only if arr[0] < arr[1] < arr[2] < ... < arr[arr.length - 1].

 

Example 1:

Input: nums1 = [1,3,5,4], nums2 = [1,2,3,7]
Output: 1
Explanation: 
Swap nums1[3] and nums2[3]. Then the sequences are:
nums1 = [1, 3, 5, 7] and nums2 = [1, 2, 3, 4]
which are both strictly increasing.

Example 2:

Input: nums1 = [0,3,5,8,9], nums2 = [2,1,4,6,9]
Output: 1

 

Constraints:

    2 <= nums1.length <= 105
    nums2.length == nums1.length
    0 <= nums1[i], nums2[i] <= 2 * 105

'''

class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        n=len(nums1)
        noswap,swap=0,1
        for i in range(1,n):
            noswap2,swap2=n,n
            if nums1[i-1]<nums1[i] and nums2[i-1]<nums2[i]:
                noswap2=min(noswap2,noswap)
                swap2=min(swap2,swap+1)
            if nums2[i-1]<nums1[i] and nums1[i-1]<nums2[i]:
                noswap2=min(noswap2,swap)
                swap2=min(swap2,noswap+1)

            noswap,swap=noswap2,swap2
        
        return min(noswap,swap)
