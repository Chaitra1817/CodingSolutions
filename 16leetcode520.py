'''
We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Given a string word, return true if the usage of capitals in it is right.

 

Example 1:

Input: word = "USA"
Output: true
'''
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word == word.upper() or word == word.lower() or word == word.title()
        
        #or
        
        word1=''
        word1=word.lower()
        word2=word.upper()
        if word==word1:
            return True
        if word==word2:
            return True
        for i in word[1:]:
            for j in i:
                if j.isupper():
                    return False
        return True
