'''
Given two version strings, version1 and version2, compare them. A version string consists of revisions separated by dots '.'. The value of the revision is its integer conversion ignoring leading zeros.

To compare version strings, compare their revision values in left-to-right order. If one of the version strings has fewer revisions, treat the missing revision values as 0.

Return the following:

    If version1 < version2, return -1.
    If version1 > version2, return 1.
    Otherwise, return 0.

 

Example 1:

Input: version1 = "1.2", version2 = "1.10"

Output: -1

Explanation:

version1's second revision is "2" and version2's second revision is "10": 2 < 10, so version1 < version2.

Example 2:

Input: version1 = "1.01", version2 = "1.001"

Output: 0

Explanation:

Ignoring leading zeroes, both "01" and "001" represent the same integer "1".

Example 3:

Input: version1 = "1.0", version2 = "1.0.0.0"

Output: 0

Explanation:

version1 has less revisions, which means every missing revision are treated as "0".

'''

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1,v2=version1.split('.'),version2.split('.')
        
        n=max(len(v1),len(v2))
        
        for i in range(n):
            n1=int(v1[i]) if i<len(v1) else 0
            n2=int(v2[i]) if i<len(v2) else 0
            
            if n1>n2:
                return 1
            elif n2>n1:
                return -1
            
        return 0

