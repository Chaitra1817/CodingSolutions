'''

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

Example 1:

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9

'''

class Solution:
    def trap(self, height):
        n = len(height)
        if n == 0:
            return 0
        
        p = [0] * n
        s = [0] * n
        
        p[0] = height[0]
        for i in range(1, n):
            p[i] = max(p[i - 1], height[i])
        
        s[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            s[i] = max(s[i + 1], height[i])
        
        ans = 0
        for i in range(n):
            ans += min(p[i], s[i]) - height[i]
        
        return ans
