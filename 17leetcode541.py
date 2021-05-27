'''
Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.

If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.

 

Example 1:

Input: s = "abcdefg", k = 2
Output: "bacdfeg"
'''

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        N = len(s)
        res = ""
        pos = 0
        while pos < N:
            nx = s[pos : pos + k]
            res = res + nx[::-1] + s[pos + k : pos + 2 * k]
            pos += 2 * k
          
        return res
        
       
    
    
    
   
