'''
1143. Longest Common Subsequence
Solved
Medium
Topics
Companies
Hint

Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

    For example, "ace" is a subsequence of "abcde".

A common subsequence of two strings is a subsequence that is common to both strings.

 

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.

Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.

'''

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n=len(text1)
        m=len(text2)

        @cache
        def findLength(text1,text2,i,j):
            if(i<0 or j<0):
                return 0
            
            if text1[i]==text2[j]:
                return 1+findLength(text1,text2,i-1,j-1)
            
            return max(findLength(text1,text2,i-1,j), findLength(text1,text2,i,j-1))

        return findLength(text1,text2,n-1,m-1)


# METHOD 2


# class Solution:
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         n=len(text1)
#         m=len(text2)
#         dp=[[-1 for i in range(m)] for j in range(n)]

#         def findLength(text1,text2,i,j):
#             if(i<0 or j<0):
#                 return 0
            
#             if dp[i][j]!=-1:
#                 return dp[i][j]
            
#             if text1[i]==text2[j]:
#                 dp[i][j]=1+findLength(text1,text2,i-1,j-1)
#                 return dp[i][j] 
            
#             dp[i][j]=max(findLength(text1,text2,i-1,j), findLength(text1,text2,i,j-1))
#             return dp[i][j]

#         return findLength(text1,text2,n-1,m-1)
        
        


