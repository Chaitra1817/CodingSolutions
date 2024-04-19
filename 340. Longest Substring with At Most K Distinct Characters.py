'''
340. Longest Substring with At Most K Distinct Characters
Solved
Medium
Topics
Companies

Given a string s and an integer k, return the length of the longest
substring
of s that contains at most k distinct characters.

 

Example 1:

Input: s = "eceba", k = 2
Output: 3
Explanation: The substring is "ece" with length 3.

Example 2:

Input: s = "aa", k = 1
Output: 2
Explanation: The substring is "aa" with length 2.

'''
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        l, r = 0, 0
        max_len = 0
        char_count = {}
        n = len(s)
        
        while r < n:
            char_count[s[r]] = r
            r += 1
            
            if len(char_count) > k:
                leftmost_index = min(char_count.values())
                del char_count[s[leftmost_index]]
                l = leftmost_index + 1
                
            max_len = max(max_len, r - l)
        
        return max_len
