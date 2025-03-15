'''
You are given an array of digits called digits. Your task is to determine the number of distinct three-digit even numbers that can be formed using these digits.

Note: Each copy of a digit can only be used once per number, and there may not be leading zeros.

 

Example 1:

Input: digits = [1,2,3,4]

Output: 12

Explanation: The 12 distinct 3-digit even numbers that can be formed are 124, 132, 134, 142, 214, 234, 312, 314, 324, 342, 412, and 432. Note that 222 cannot be formed because there is only 1 copy of the digit 2.

Example 2:

Input: digits = [0,2,2]

Output: 2

Explanation: The only 3-digit even numbers that can be formed are 202 and 220. Note that the digit 2 can be used twice because it appears twice in the array.

Example 3:

Input: digits = [6,6,6]

Output: 1

Explanation: Only 666 can be formed.©leetcode

'''


from collections import Counter
from typing import List

class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        d = Counter(digits)  
        even_digits = [x for x in d if x % 2 == 0] 
        cnt = 0

        for last in even_digits:  
            d[last] -= 1  
            
            for first in d:  
                if first == 0 or d[first] == 0:
                    continue  
                
                d[first] -= 1  

                for middle in d:  
                    if d[middle] > 0:  
                        cnt += 1

                d[first] += 1  

            d[last] += 1  
        
        return cnt

©leetcode
