'''
239. Sliding Window Maximum
Solved
Hard
Topics
Companies
Hint

You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

 

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Example 2:

Input: nums = [1], k = 1
Output: [1]

'''

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r = 0, 0 
        q = collections.deque()  # deque to store indices of elements in the current window
        ans = []  

        while r < len(nums):
            # Remove elements from the back of the deque if they are smaller than the current element
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # If the left pointer is outside the current window, remove its index from the front of the deque(since we don't need it)
            if l > q[0]:
                q.popleft()

            # If the window size is reached, add the maximum element in the current window to the result list
            if (r + 1) >= k:
                ans.append(nums[q[0]])
                l += 1

            r += 1

        return ans
