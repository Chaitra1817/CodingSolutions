'''
Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

Return any possible rearrangement of s or return "" if not possible.

 

Example 1:

Input: s = "aab"
Output: "aba"

Example 2:

Input: s = "aaab"
Output: ""

 

Constraints:

    1 <= s.length <= 500
    s consists of lowercase English letters.

'''

class Solution:
    def reorganizeString(self, s: str) -> str:
        d=Counter(s)

        mxfreq=max(d.values())
        if mxfreq>(len(s)+1)//2:
            return ""

        hp=[[-cnt,char] for char,cnt in d.items()]
        heapq.heapify(hp)
        res=""
        prev=None

        while hp:
            cnt,char=heapq.heappop(hp)
            res+=char
            cnt+=1

            if prev:
                heapq.heappush(hp,prev)
                prev=None
            
            if cnt!=0:
                prev=[cnt,char]
            
        return res

        

        
