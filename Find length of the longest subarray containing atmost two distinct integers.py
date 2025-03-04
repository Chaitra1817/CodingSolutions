'''
Given an array arr[] containing positive elements, the task is to find the length of the longest subarray of an input array containing at most two distinct integers.

Examples:

Input: arr[]= [2, 1, 2]
Output: 3
Explanation: The entire array [2, 1, 2] contains at most two distinct integers (2 and 1). Hence, the length of the longest subarray is 3.

Input: arr[] = [3, 1, 2, 2, 2, 2]
Output: 5
Explanation: The longest subarray containing at most two distinct integers is [1, 2, 2, 2, 2], which has a length of 5. The subarray starts at the second element 1 and ends at the last element. It contains at most two distinct integers (1 and 2).

Constraints:
1 ≤ arr.size() ≤ 105
1 ≤ arr[i] <=105

'''

class Solution:
    def totalElements(self, arr):
        n = len(arr)
        s = set()
        l, r = 0, 0
        max_len = 0

        while r < n:
            if arr[r] in s or len(s) < 2:
                s.add(arr[r])        
                max_len = max(max_len, r - l + 1)
                r += 1              
            else:
                while len(s) == 2:
                    s.discard(arr[l])
                    l += 1
                    s = set(arr[l:r])
        return max_len
