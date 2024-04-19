'''

3. Longest Substring Without Repeating Characters
Solved
Medium
Topics
Companies

Given a string s, find the length of the longest
substring
without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

 '''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        max_len = 0
        n = len(s)
        d = {}

        while r < n:
            if s[r] not in d or d[s[r]] < l:
                d[s[r]] = r
                max_len = max(max_len, r - l + 1)
                r += 1
            else:
                l = d[s[r]] + 1
                d[s[r]] = r
                r += 1

        return max_len
