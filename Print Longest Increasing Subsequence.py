'''
Given an integer n and an array of integers arr, return the Longest Increasing Subsequence which is Index-wise lexicographically smallest.
Note - A subsequence S1 is Index-wise lexicographically smaller than a subsequence S2 if in the first position where S1 and S2 differ, subsequence S1 has an element that appears earlier in the array  arr than the corresponding element in S2.
LIS  of a given sequence is defined as that longest possible subsequence all of whose elements are in increasing order. For example, the length of LIS for {10, 22, 9, 33, 21, 50, 41, 60, 80} is 6 and the LIS is {10, 22, 33, 50, 60, 80}. 

Example 1:

Input:
n = 16
arr = [0,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15]
Output:
0 4 6 9 13 15 
Explanation:
longest Increasing subsequence is 0 4 6 9 13 15  and the length of the longest increasing subsequence is 6.

Example 2:

Input:
n = 1
arr = [1]
Output:
1

Your Task:
You don't need to read input or print anything. Your task is to complete the function longestIncreasingSubsequence() which takes integer n and array arr and returns the longest increasing subsequence.

Expected Time Complexity: O(n2)
Expected Space Complexity: O(n)

Constraint:
1 <= n < = 103
0 <= arr[i] <= 109

'''


class Solution:
    def longestIncreasingSubsequence(self, n, arr):
        dp=[1]*n
        prev=[-1]*n
        
        mx=0
        mxIdx=0
        for i in range(1,n):
            for j in range(i):
                if arr[j]<arr[i] and dp[j]+1>dp[i]:
                    dp[i]=dp[j]+1
                    prev[i]=j
                    
            if dp[i]>mx:
                mx=dp[i]
                mxIdx=i
        
        ans=[]
        while mxIdx!=-1:
            ans.append(arr[mxIdx])
            mxIdx=prev[mxIdx]
        
        ans.reverse()
        return ans
