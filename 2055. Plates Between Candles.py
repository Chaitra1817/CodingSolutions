'''
There is a long table with a line of plates and candles arranged on top of it. You are given a 0-indexed string s consisting of characters '*' and '|' only, where a '*' represents a plate and a '|' represents a candle.

You are also given a 0-indexed 2D integer array queries where queries[i] = [lefti, righti] denotes the substring s[lefti...righti] (inclusive). For each query, you need to find the number of plates between candles that are in the substring. A plate is considered between candles if there is at least one candle to its left and at least one candle to its right in the substring.

    For example, s = "||**||**|*", and a query [3, 8] denotes the substring "*||**|". The number of plates between candles in this substring is 2, as each of the two plates has at least one candle in the substring to its left and right.

Return an integer array answer where answer[i] is the answer to the ith query.

 

Example 1:
ex-1

Input: s = "**|**|***|", queries = [[2,5],[5,9]]
Output: [2,3]
Explanation:
- queries[0] has two plates between candles.
- queries[1] has three plates between candles.

Example 2:
ex-2

Input: s = "***|**|*****|**||**|*", queries = [[1,17],[4,5],[14,17],[5,11],[15,16]]
Output: [9,0,0,0,0]
Explanation:
- queries[0] has nine plates between candles.
- The other queries have zero plates between candles.

'''

from typing import List

class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        
        # Precompute prefix sums for plates (*) and nearest candles
        prefix_sum = [0] * n
        nearest_left_candle = [-1] * n
        nearest_right_candle = [-1] * n

        count = 0
        for i in range(n):
            if s[i] == '*':
                count += 1
            prefix_sum[i] = count
        
        # Nearest left candle
        candle_position = -1
        for i in range(n):
            if s[i] == '|':
                candle_position = i
            nearest_left_candle[i] = candle_position

        # Nearest right candle
        candle_position = -1
        for i in range(n - 1, -1, -1):
            if s[i] == '|':
                candle_position = i
            nearest_right_candle[i] = candle_position

        result = []
        for l, r in queries:
            left = nearest_right_candle[l]
            right = nearest_left_candle[r]
            
            if left == -1 or right == -1 or left >= right:
                result.append(0)
            else:
                result.append(prefix_sum[right] - prefix_sum[left])

        return result


# # TLE
# class Solution:
#     def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
#         def find(l, r):
#             while l <= r and s[l] != "|":
#                 l += 1
#             while r >= l and s[r] != "|":
#                 r -= 1
#             if l < r:
#                 plate_count = s[l+1:r].count("*")
#                 return plate_count
#             return 0

#         ans = []
#         for i, j in queries:
#             res = find(i, j)
#             ans.append(res)
#         return ans
