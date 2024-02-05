'''
Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:

Input: s = "leetcode"
Output: 0

Example 2:

Input: s = "loveleetcode"
Output: 2

Example 3:

Input: s = "aabb"
Output: -1

'''

class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = defaultdict(lambda: [0, -1])
        for i in range(len(s)):
            d[s[i]][0] += 1
            d[s[i]][1] = i
        
        ans=-1
        for k,v in d.items():
            if v[0]==1:
                return v[1]
        
        return ans
        
