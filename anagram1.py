'''
Minimum Number of Steps to Make Two Strings Anagram

Given two equal-size strings s and t. In one step you can choose any character of t and replace it with another character.

Return the minimum number of steps to make t an anagram of s.

An Anagram of a string is a string that contains the same characters with a different (or the same) ordering.

Input: s = "bab", t = "aba"
Output: 1
Explanation: Replace the first 'a' in t with b, t = "bba" which is anagram of s.
Example 2:

Input: s = "leetcode", t = "practice"
Output: 5
Explanation: Replace 'p', 'r', 'a', 'i' and 'c' from t with proper characters to make t anagram of s.

'''

 class Solution:
    def minSteps(self, s: str, t: str) -> int:
        d={}
        count=0
        #counting the frequency of charcters in the first string
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]]=1
            else:
                d[s[i]]+=1
        
        for i in range(len(t)):
            #if that character exist in the dictionary decrement the value to avoid the ambiguity
            if t[i] in d and d[t[i]]>0:
                d[t[i]]-=1
            else:
            #increment the count to get the answer
                count+=1
        
        return count
        