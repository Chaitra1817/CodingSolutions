'''
540. Single Element in a Sorted Array
Solved
Medium
Topics
Companies

You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.

 

Example 1:

Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2

Example 2:

Input: nums = [3,3,7,7,10,11,11]
Output: 10

'''
class Solution:
    def singleNonDuplicate(self, arr: List[int]) -> int:
        n = len(arr)  # Size of the array

        # Edge cases:
        if n == 1:
            return arr[0]
        if arr[0] != arr[1]:
            return arr[0]
        if arr[n - 1] != arr[n - 2]:
            return arr[n - 1]

        low = 1
        high = n - 2
        while low <= high:
            mid = (low + high) // 2

            # If arr[mid] is the single element:
            if arr[mid] != arr[mid + 1] and arr[mid] != arr[mid - 1]:
                return arr[mid]

            # We are in the left:
            if (mid % 2 == 1 and arr[mid] == arr[mid - 1]) or (mid % 2 == 0 and arr[mid] == arr[mid + 1]):
                # Eliminate the left half:
                low = mid + 1
            # We are in the right:
            else:
                # Eliminate the right half:
                high = mid - 1

        # Dummy return statement:
        return -1


