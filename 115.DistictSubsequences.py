'''
115. Distinct Subsequences
Solved
Hard
Topics
Companies

Given two strings s and t, return the number of distinct subsequences of s which equals t.

The test cases are generated so that the answer fits on a 32-bit signed integer.

 

Example 1:

Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from s.
rabbbit
rabbbit
rabbbit

Example 2:

Input: s = "babgbag", t = "bag"
Output: 5
Explanation:
As shown below, there are 5 ways you can generate "bag" from s.
babgbag
babgbag
babgbag
babgbag
babgbag

'''

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n,m=len(s),len(t)

        @cache
        def findWays(i,j,s,t):
            if j<0:
                return 1
            if i<0:
                return 0
            if s[i]==t[j]:
                return findWays(i-1,j-1,s,t)+findWays(i-1,j,s,t)
            
            return findWays(i-1,j,s,t)

        return findWays(n-1,m-1,s,t)
        

