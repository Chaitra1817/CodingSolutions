'''
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 

Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
'''

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m,n=len(s1),len(s2)
        if m>n:
            return False
        
        s1_d=Counter(s1)
        s2_d=defaultdict(int)
        l=0
        r=0
        while r<n:
            if s2[r] not in s1_d:
                r+=1
                l=r
                s2_d.clear()
                continue

            s2_d[s2[r]]+=1

            while s2_d[s2[r]]>s1_d[s2[r]]:
                l_ch=s2[l]
                s2_d[l_ch]-=1
                l+=1

            found=True
            if r-l+1==m:
                for k,v in s1_d.items():
                    if v==s2_d[k]:
                        continue
                    else:
                        found=False
                        break
                if found:
                    return True

            r+=1

        return False
        
