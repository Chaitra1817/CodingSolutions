
'''
516. Longest Palindromic Subsequence
Solved
Medium
Topics
Companies

Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

 

Example 1:

Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".

Example 2:

Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".

 

Constraints:

    1 <= s.length <= 1000
    s consists only of lowercase English letters.

'''
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # Same as longest common subsequence
        # ans=0
        # s1=s[::-1]
        # m=len(s)
        # n=m

        # dp=[[-1 for i in range(m)]for j in range(n)]
        # def findLps(m,n):
        #     nonlocal s1
        #     if m<0 or n<0:
        #         return 0

        #     if dp[m][n]!=-1:
        #         return dp[m][n]

        #     if s[m]==s1[n]:
        #         dp[m][n]= 1+findLps(m-1,n-1)
        #         return dp[m][n]
            
        #     dp[m][n]= max(findLps(m-1,n),findLps(m,n-1))
        #     return dp[m][n]
        
        # return findLps(m-1,n-1)



        # n = len(s)
        
        # memo = {}
        # def lps(l, r):
        #     print("memo",memo)
        #     if (l,r) in memo:
        #         return memo[(l,r)]
        #     if l > r:
        #         return 0
        #     if l == r:
        #         return 1

        #     if s[l] == s[r]:
        #         memo[(l,r)] = lps(l + 1, r - 1) + 2
        #     else:
        #         memo[(l,r)] = max(lps(l, r - 1), lps(l + 1, r))
        #     return memo[(l, r)]

        # return lps(0, n - 1)

       
        n = len(s)
        s1 = s[::-1]  
        dp = [[0] * (n + 1) for _ in range(n + 1)]  

        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if s[i - 1] == s1[j - 1]:  
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:  
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[n][n]
