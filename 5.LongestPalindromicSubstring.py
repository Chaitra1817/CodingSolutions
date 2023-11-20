'''

5. Longest Palindromic Substring
Solved
Medium
Topics
Companies
Hint

Given a string s, return the longest
palindromic
substring
in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:

Input: s = "cbbd"
Output: "bb"

 

Constraints:

    1 <= s.length <= 1000
    s consist of only digits and English letters.

'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans=""
        length=-1
        for i in range(len(s)-1):
            for j in range(i+1,len(s)):
                s1=s[i:j+1]
                s2=s1[::-1]
                if s1==s2 and (j-i+1 > length):
                    length=j-i+1
                    ans=s1
        
        if ans=="":
            return s[0]
        return ans
                    

        

