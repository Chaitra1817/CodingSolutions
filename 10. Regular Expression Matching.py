'''
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

    '.' Matches any single character.​​​​
    '*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

 

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:

Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

Example 3:

Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".

 

Constraints:

    1 <= s.length <= 20
    1 <= p.length <= 20
    s contains only lowercase English letters.
    p contains only lowercase English letters, '.', and '*'.
    It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.


 '''

'''
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        memo = {}

        def find(i, j):
            if i < 0 and j < 0:
                return True
            if j < 0:
                return False
            if i < 0:
                return find(i, j - 2) if p[j] == '*' else False

            if (i, j) in memo:
                return memo[(i, j)]

            take = False
            notTake = False

            if p[j] == '*':
                notTake = find(i, j - 2)
                if p[j-1]==s[i] or p[j-1]==".":
                    notTake |= find(i-1,j)
                
            else:
                if p[j] == s[i] or p[j] == '.':
                    take = find(i - 1, j - 1)

            memo[(i, j)] = take or notTake
            return memo[(i, j)]

        return find(m - 1, n - 1)

'''

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n+1) for _ in range(m+1)]

        dp[0][0]=True

        for j in range(2, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        for i in range(1,m+1):
            for j in range(1,n+1):
                if p[j-1]=="*":
                    if j-2>=0:
                        dp[i][j] = dp[i][j - 2]
                        if p[j-2]==s[i-1] or p[j-2]==".":
                            dp[i][j]|=dp[i-1][j]
                else:
                    if p[j-1] == s[i-1] or p[j-1] == '.':
                        dp[i][j] = dp[i - 1][j - 1]

        return dp[m][n]

