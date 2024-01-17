'''
583. Delete Operation for Two Strings
Solved
Medium
Topics
Companies

Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.

In one step, you can delete exactly one character in either string.

 

Example 1:

Input: word1 = "sea", word2 = "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".

Example 2:

Input: word1 = "leetcode", word2 = "etco"
Output: 4

'''

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m=len(word1)
        n=len(word2)
        memo=[[-1 for j in range(n)]for i in range(m+1)]

        def findSteps(i,j):
            nonlocal word1,word2,memo
            if i<0 or j<0:
                return 0
            
            if word1[i]==word2[j]:
                return 1+findSteps(i-1,j-1)
            
            if memo[i][j]!=-1:
                return memo[i][j]
            
            memo[i][j]=max(findSteps(i-1,j),findSteps(i,j-1))
            return memo[i][j]
        
        l=findSteps(m-1,n-1)
        return m+n-(2*l)
