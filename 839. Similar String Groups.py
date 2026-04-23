'''
Two strings, X and Y, are considered similar if either they are identical or we can make them equivalent by swapping at most two letters (in distinct positions) within the string X.

For example, "tars" and "rats" are similar (swapping at positions 0 and 2), and "rats" and "arts" are similar, but "star" is not similar to "tars", "rats", or "arts".

Together, these form two connected groups by similarity: {"tars", "rats", "arts"} and {"star"}.  Notice that "tars" and "arts" are in the same group even though they are not similar.  Formally, each group is such that a word is in the group if and only if it is similar to at least one other word in the group.

We are given a list strs of strings where every string in strs is an anagram of every other string in strs. How many groups are there?

 

Example 1:

Input: strs = ["tars","rats","arts","star"]
Output: 2
Example 2:

Input: strs = ["omv","ovm"]
Output: 1
 

Constraints:

1 <= strs.length <= 300
1 <= strs[i].length <= 300
strs[i] consists of lowercase letters only.
All words in strs have the same length and are anagrams of each other.
'''

''''
#Approach 1
class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n=len(strs)
        d=defaultdict(list)

        def compare(s1,s2):
            cnt=0
            for i in range(len(s1)):
                if s1[i]==s2[i]:
                    pass
                else:
                    cnt+=1

            if cnt==2 or cnt==0:
                d[s1].append(s2)
                d[s2].append(s1)

        for i in range(n-1):
            for j in range(i+1,n):
                compare(strs[i],strs[j])

        def find(word):
            visited.add(word)
            for val in d[word]:
                if val not in visited:
                    find(val)
        
        ans=0
        visited=set()
        for word in strs:
            if word not in visited:
                ans+=1
                find(word)
        return ans

TC: O(n^2 * m)
SC: O(n^2)

'''

class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        n=len(strs)
        parent=list(range(n))

        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]

        def union(x,y):
            ulpx,ulpy=find(x),find(y)
            if ulpx!=ulpy:
                parent[ulpx]=ulpy
        
        def similar(s1,s2):
            diff=0
            for c1,c2 in zip(s1,s2):
                if c1!=c2:
                    diff+=1
                    if diff>2:
                        return False
            return diff==0 or diff<=2

        for i in range(n-1):
            for j in range(i+1,n):
                if similar(strs[i],strs[j]):
                    union(i,j)
        visited=set()
        for i in range(n):
            visited.add(find(i))
        return len(visited)


'''
TC:o(n^2*m)
SC:o(n)
