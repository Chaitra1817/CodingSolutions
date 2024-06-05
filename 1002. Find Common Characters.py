'''
1002. Find Common Characters
Solved
Easy
Topics
Companies

Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

 

Example 1:

Input: words = ["bella","label","roller"]
Output: ["e","l","l"]

Example 2:

Input: words = ["cool","lock","cook"]
Output: ["c","o"]

 

Constraints:

    1 <= words.length <= 100
    1 <= words[i].length <= 100
    words[i] consists of lowercase English letters.

'''

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common=Counter(words[0])
        res=[]
        for i in words[1:]:
            cur=Counter(i)
            for letter in common.keys():
                common[letter]=min(common[letter],cur[letter])
        
        for k,v in common.items():
            for i in range(v):
                res.append(k)
        
        return res
