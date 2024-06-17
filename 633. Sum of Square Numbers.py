'''
633. Sum of Square Numbers
Solved
Medium
Topics
Companies

Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.

 

Example 1:

Input: c = 5
Output: true
Explanation: 1 * 1 + 2 * 2 = 5

Example 2:

Input: c = 3
Output: false

 

Constraints:

    0 <= c <= 231 - 1

'''
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # Approach 1
        # left = 0
        # right = int(math.sqrt(c))
        # while left <= right:
        #     current_sum = left * left + right * right
        #     if current_sum == c:
        #         return True
        #     elif current_sum < c:
        #         left += 1
        #     else:
        #         right -= 1
        
        # return False

        # Approach 2
        for a in range(int(math.sqrt(c)) + 1):  # Include the upper bound
            b = math.sqrt(c - a * a)
            if b == int(b):  # Check if b is an integer
                return True
        return False
