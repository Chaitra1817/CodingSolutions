'''
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

    '?' Matches any single character.
    '*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

 

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:

Input: s = "aa", p = "*"
Output: true
Explanation: '*' matches any sequence.

Example 3:

Input: s = "cb", p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.

 '''

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m,n=len(p),len(s)

        @cache
        def find(i,j):
            nonlocal s,p
            if i<0 and j<0:
                return True
            elif i<0:
                return False
            elif j<0 and i>=0:
                for k in range(i+1):
                    if p[k]!='*':
                        return False
                return True

            if p[i]==s[j] or p[i]=='?':
                return find(i-1,j-1)
            
            if p[i]=='*':
                return find(i-1,j) or find(i,j-1)
            return False

        return find(m-1,n-1)        
