'''
You are given an array of strings arr. A string s is formed by the concatenation of a subsequence of arr that has unique characters.

Return the maximum possible length of s.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

 

Example 1:

Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All the valid concatenations are:
- ""
- "un"
- "iq"
- "ue"
- "uniq" ("un" + "iq")
- "ique" ("iq" + "ue")
Maximum length is 4.

Example 2:

Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible longest valid concatenations are "chaers" ("cha" + "ers") and "acters" ("act" + "ers").

Example 3:

Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26
Explanation: The only string in arr has all 26 characters.

'''

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        n = len(arr)
        def traverse(idx, s = set(), l = 0):
            if idx >= n: return l
            curr = arr[idx]
            currs = set(curr)
            if len(currs) < len(curr): 
                return traverse(idx + 1, s, l)
            if currs & s: 
                return traverse(idx + 1, s, l)
            return max(traverse(idx + 1, s | currs, l + len(curr)), traverse(idx + 1, s, l))

        return traverse(0)     
