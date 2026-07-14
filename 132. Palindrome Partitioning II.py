'''
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

 

Example 1:

Input: s = "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
Example 2:

Input: s = "a"
Output: 0
Example 3:

Input: s = "ab"
Output: 1
 

Constraints:

1 <= s.length <= 2000
s consists of lowercase English letters only.
'''

class Solution:
    def minCut(self, s):
        n=len(s)

        def isPalindrome(start,end,s):
            return s[start:end+1]==s[start:end+1][::-1]

        memo={}
        def find(i,n,s):
            if i==n:
                return 0
            
            if (i,n) in memo:
                return memo[(i,n)]
            
            ans=float('inf')
            for idx in range(i,n):
                if isPalindrome(i,idx,s):
                    cur=1+find(idx+1,n,s)
                    ans=min(ans,cur)
            memo[(i,n)] = ans
            return memo[(i,n)]

        return find(0,n,s)-1
