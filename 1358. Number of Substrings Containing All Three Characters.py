'''

Given a string s consisting only of characters a, b and c.

Return the number of substrings containing at least one occurrence of all these characters a, b and c.

 

Example 1:

Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). 

Example 2:

Input: s = "aaacb"
Output: 3
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb". 

Example 3:

Input: s = "abc"
Output: 1

'''

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        d = {'a': -1, 'b': -1, 'c': -1}  
        ans = 0
        for i, ch in enumerate(s):
            d[ch] = i
            if d['a'] != -1 and d['b'] != -1 and d['c'] != -1:
                mn = min(d['a'], d['b'], d['c'])
                ans += mn + 1
        return ans
