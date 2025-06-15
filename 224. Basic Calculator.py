'''
Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

 

Example 1:

Input: s = "1 + 1"
Output: 2

Example 2:

Input: s = " 2-1 + 2 "
Output: 3

Example 3:

Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23

'''
class Solution:
    def calculate(self, s: str) -> int:
        res=0
        cur=0
        sign=1
        stack=[]

        for i in s:
            if i.isdigit():
                cur=cur*10+int(i)
            elif i=="+":
                res+=sign*cur
                cur=0
                sign=1
            elif i=="-":
                res+=sign*cur
                cur=0
                sign=-1
            elif i=="(":
                stack.append([res,sign])
                res=0
                sign=1
                cur=0
            elif i==")":
                res+=sign*cur
                prevres,prevsign=stack.pop()
                res=prevres+prevsign*res
                cur=0
                sign=1
        return res+sign*cur



            
