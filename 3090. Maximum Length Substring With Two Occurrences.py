'''
Given a string s, return the maximum length of a
substring
 such that it contains at most two occurrences of each character.

 

Example 1:

Input: s = "bcbbbcba"

Output: 4

Explanation:
The following substring has a length of 4 and contains at most two occurrences of each character: "bcbbbcba".

Example 2:

Input: s = "aaaa"

Output: 2

Explanation:
The following substring has a length of 2 and contains at most two occurrences of each character: "aaaa".

 '''

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        left,right,max_length=0,0,0
        d={}

        while right<len(s):
            d[s[right]]=d.get(s[right],0)+1

            while d[s[right]]>2:
                d[s[left]]-=1
                if d[s[left]]==0:
                    del d[s[left]]
                left+=1

            max_length=max(max_length,right-left+1)
            right+=1
        
        return max_length
