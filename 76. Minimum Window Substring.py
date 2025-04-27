'''

Given two strings s and t of lengths m and n respectively, return the minimum window

of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.


 '''

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        m = len(t)

        d = {}
        for char in t:
            d[char] = d.get(char, 0) + 1
        
        l, r = 0, 0
        minlen = float('inf')
        startIdx = -1
        cnt = 0  
        required = len(d)  
        
        while r < n:
            if s[r] in d:
                d[s[r]] -= 1
                if d[s[r]] == 0:  
                    cnt += 1
            
            while cnt == required:
                if r - l + 1 < minlen:
                    minlen = r - l + 1
                    startIdx = l
                
                if s[l] in d:
                    d[s[l]] += 1
                    if d[s[l]] > 0:  
                        cnt -= 1
                l += 1
            
            r += 1
        
        return s[startIdx:startIdx + minlen] if minlen != float('inf') else ""
