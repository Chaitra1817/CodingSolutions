'''
Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

 

Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".
'''

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_t=[]
        stack_s=[]
        def final_string(stk,string):
            for char in string:
                if char!='#':
                    stk.append(char)
                elif stk:
                    stk.pop()
            return ''.join(stk)
        return final_string(stack_s,s)==final_string(stack_t,t)
                    
        
        
        
      
