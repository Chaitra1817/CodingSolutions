'''
1312. Minimum Insertion Steps to Make a String Palindrome
Solved
Hard
Topics
Companies
Hint

Given a string s. In one step you can insert any character at any index of the string.

Return the minimum number of steps to make s palindrome.

A Palindrome String is one that reads the same backward as well as forward.

 

Example 1:

Input: s = "zzazz"
Output: 0
Explanation: The string "zzazz" is already palindrome we do not need any insertions.

Example 2:

Input: s = "mbadm"
Output: 2
Explanation: String can be "mbdadbm" or "mdbabdm".

Example 3:

Input: s = "leetcode"
Output: 5
Explanation: Inserting 5 characters the string becomes "leetcodocteel".

'''

class Solution:
    def minInsertions(self, s: str) -> int:
        s1=s[::-1]
        n=len(s)
        memo=[[-1 for j in range(n)]for i in range(n+1)]
        def findSteps(i,j):
            nonlocal s,s1,memo
            if i<0 or j<0:
                return 0
            
            if memo[i][j]!=-1:
                return memo[i][j]
        
            if s[i]==s1[j]:
                return 1+findSteps(i-1,j-1)
            
            memo[i][j]= max(findSteps(i,j-1),findSteps(i-1,j))
            return memo[i][j]
        
        l=findSteps(n-1,n-1)
        return len(s)-l
        
