'''

You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part. For example, the string "ababcc" can be partitioned into ["abab", "cc"], but partitions such as ["aba", "bcc"] or ["ab", "ab", "cc"] are invalid.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

Return a list of integers representing the size of these parts.

 

Example 1:

Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.

Example 2:

Input: s = "eccbbbbdec"
Output: [10]


'''

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_seen=[0]*26
        for i,chr in enumerate(s):
            last_seen[ord(chr)-ord('a')]=i
        
        partition_end=0
        partition_start=0
        ans=[]
        for i,chr in enumerate(s):
            partition_end=max(partition_end,last_seen[ord(chr)-ord('a')])
            if i==partition_end:
                ans.append(partition_end-partition_start+1)
                partition_start=i+1

        return ans
