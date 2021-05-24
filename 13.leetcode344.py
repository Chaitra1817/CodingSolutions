'''
Write a function that reverses a string. The input string is given as an array of characters s.


Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Follow up: Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

'''

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i=0
        j=len(s)-1
        while i<=j:
          s[i],s[j]=s[j],s[i]
          i+=1
          j-=1
        
      
        '''
        or  s[:]=s[::-1]
        '''
        
