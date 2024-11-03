'''
3340. Check Balanced String
Solved
Easy
Companies

You are given a string num consisting of only digits. A string of digits is called balanced if the sum of the digits at even indices is equal to the sum of digits at odd indices.

Return true if num is balanced, otherwise return false.

 

Example 1:

Input: num = "1234"

Output: false

Explanation:

    The sum of digits at even indices is 1 + 3 == 4, and the sum of digits at odd indices is 2 + 4 == 6.
    Since 4 is not equal to 6, num is not balanced.

'''
class Solution:
    def isBalanced(self, num: str) -> bool:
        e,o=0,0
        for i in range(len(num)):
            if i%2==0:
                e+=int(num[i])
            else:
                o+=int(num[i])
        return e==o

class Solution:
    def isBalanced(self, num: str) -> bool:
        x = sum(int(x) for x in num[0::2])
        y = sum(int(x) for x in num[1::2])
        return x==y
        
        
class Solution:
    def isBalanced(self, num: str) -> bool:
        return sum(map(int, num[::2])) == sum(map(int, num[1::2]))
