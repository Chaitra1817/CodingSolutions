'''
You are given a 2D integer array squares. Each squares[i] = [xi, yi, li] represents the coordinates of the bottom-left point and the side length of a square parallel to the x-axis.

Find the minimum y-coordinate value of a horizontal line such that the total area of the squares above the line equals the total area of the squares below the line.

Answers within 10-5 of the actual answer will be accepted.

Note: Squares may overlap. Overlapping areas should be counted multiple times.

 

Example 1:

Input: squares = [[0,0,1],[2,2,1]]

Output: 1.00000
'''

from typing import List

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        # Set the initial search range
        low = min(y for _, y, _ in squares)  # Smallest bottom y-coordinate
        high = max(y + l for _, y, l in squares)  # Highest top y-coordinate

        # Function to calculate the area above and below a given y = mid
        def compute_balance(mid):
            area_above = 0
            area_below = 0
            
            for x, y, l in squares:
                top = y + l  # Top boundary of the square
                
                if top <= mid:  
                    # Entire square is below the line
                    area_below += l * l  
                elif y >= mid:  
                    # Entire square is above the line
                    area_above += l * l  
                else:  
                    # Square is partially split by `mid`
                    below_part = (mid - y) * l  # Part below `mid`
                    above_part = (top - mid) * l  # Part above `mid`
                    area_below += below_part
                    area_above += above_part

            return area_above - area_below  # Positive if more area above, negative if more below

        # Binary search to find the correct y-coordinate
        while (high - low) > 1e-5:
            mid = (low + high) / 2
            balance = compute_balance(mid)

            if balance > 0:  
                low = mid  # Move up
            else:  
                high = mid  # Move down

        return round(high, 5)  # Return the result rounded to 5 decimal places
