'''

438. Find All Anagrams in a String
Solved
Medium
Topics
Companies

Given two strings s and p, return an array of all the start indices of p's

in s. You may return the answer in any order.

 

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".

 

Constraints:

    1 <= s.length, p.length <= 3 * 104
    s and p consist of lowercase English letters.

'''

from typing import List
from collections import Counter, defaultdict

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n=len(s)
        pd=Counter(p)
        sd=defaultdict(int)
        l,r=0,0
        res=[]
        while r<n:
            sd[s[r]]+=1
            if(r-l+1)>len(p):
                sd[s[l]]-=1
                if sd[s[l]]==0:
                    del sd[s[l]]
                l+=1
            if sd==pd:
                res.append(l)
            r+=1

        return res
