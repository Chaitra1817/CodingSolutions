'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true

'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for ch in s:
            if ch in ['(', '[', '{']:
                stack.append(ch)
            else:
                if stack:
                    last = stack.pop()
                else:
                    return False
                
                if ((ch == ')' and last == '(') 
                    or (ch == ']' and last == '[')
                    or (ch == '}' and last == '{')):
                    continue
                else:
                    return False
        return len(stack) == 0
            
        
        
