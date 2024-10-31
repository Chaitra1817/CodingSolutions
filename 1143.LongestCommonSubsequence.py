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
        n = len(text1)
        m = len(text2)
        
        # Initialize dp array with size (n+1) x (m+1) with all values set to 0
        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
        
        # Fill the dp array
        for i in range(1, n+1):
            for j in range(1, m+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        # The bottom-right cell contains the length of the longest common subsequence
        return dp[n][m]



# class Solution:
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         n=len(text1)
#         m=len(text2)
#         dp=[[-1 for i in range(m)] for j in range(n)]
#         def findLength(i,j):
#             if(i>=n or j>=m):
#                 return 0

#             if dp[i][j]!=-1:
#                 return dp[i][j]

#             if text1[i]==text2[j]:
#                 return 1+findLength(i+1,j+1)
            
#             dp[i][j] = max(findLength(i+1,j), findLength(i,j+1))
#             return dp[i][j]
#         return findLength(0,0)


# class Solution:
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         n=len(text1)
#         m=len(text2)

#         @cache
#         def findLength(text1,text2,i,j):
#             if(i<0 or j<0):
#                 return 0
            
#             if text1[i]==text2[j]:
#                 return 1+findLength(text1,text2,i-1,j-1)
            
#             return max(findLength(text1,text2,i-1,j), findLength(text1,text2,i,j-1))

#         return findLength(text1,text2,n-1,m-1)

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
        
        
