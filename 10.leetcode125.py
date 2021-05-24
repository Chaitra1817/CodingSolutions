'''
Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        
        new_str=''
        for i in s:
            if i.isalnum():
                new_str+=i
        return new_str==new_str[::-1]
