'''
14. Longest Common Prefix
Easy
16.3K
4.3K
company
Amazon
company
Apple
company
Google

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # ans=strs[0]
        # for i in strs:
        #     while not i.startswith(ans):
        #         ans=ans[:-1]
        # return ans

        if not strs:
            return ""
        
        # Find the shortest string in the list
        min_len = min(len(s) for s in strs)
        
        # Compare characters of the shortest string with other strings
        for i in range(min_len):
            char = strs[0][i]
            for s in strs[1:]:
                if s[i] != char:
                    return strs[0][:i]
        
        return strs[0][:min_len]



