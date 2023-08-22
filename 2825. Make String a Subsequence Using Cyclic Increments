"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
"""


class Solution:
    def checkIncrement(self, ch) :
        asc = ord(ch)
        if ch == 'z':
            return 'a'
        else:
            return chr(asc + 1)
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        ind = 0
        for ch in str1:
            if ch == str2[ind] or self.checkIncrement(ch) == str2[ind]:
                ind += 1
            if ind == len(str2):
                return True
        return False
        
