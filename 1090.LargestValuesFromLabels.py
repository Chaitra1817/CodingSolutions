'''
1090. Largest Values From Labels
Medium
Topics
Companies
Hint

There is a set of n items. You are given two integer arrays values and labels where the value and the label of the ith element are values[i] and labels[i] respectively. You are also given two integers numWanted and useLimit.

Choose a subset s of the n elements such that:

    The size of the subset s is less than or equal to numWanted.
    There are at most useLimit items with the same label in s.

The score of a subset is the sum of the values in the subset.

Return the maximum score of a subset s.

 

Example 1:

Input: values = [5,4,3,2,1], labels = [1,1,2,2,3], numWanted = 3, useLimit = 1
Output: 9
Explanation: The subset chosen is the first, third, and fifth items.

Example 2:

Input: values = [5,4,3,2,1], labels = [1,3,3,3,2], numWanted = 3, useLimit = 2
Output: 12
Explanation: The subset chosen is the first, second, and third items.

Example 3:

Input: values = [9,8,8,7,6], labels = [0,0,0,1,1], numWanted = 3, useLimit = 1
Output: 16
Explanation: The subset chosen is the first and fourth items.

'''

class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        ans = 0 
        freq = defaultdict(int)
        for value, label in sorted(zip(values, labels), reverse=True): 
            if 0 < num_wanted and freq[label] < use_limit: 
                ans += value
                num_wanted -= 1
                freq[label] += 1
        return ans 
