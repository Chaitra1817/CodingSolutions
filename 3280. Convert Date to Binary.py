'''
3280. Convert Date to Binary
Solved
Easy
Topics
Companies

You are given a string date representing a Gregorian calendar date in the yyyy-mm-dd format.

date can be written in its binary representation obtained by converting year, month, and day to their binary representations without any leading zeroes and writing them down in year-month-day format.

Return the binary representation of date.

 

Example 1:

Input: date = "2080-02-29"

Output: "100000100000-10-11101"

Explanation:

100000100000, 10, and 11101 are the binary representations of 2080, 02, and 29 respectively.

Example 2:

Input: date = "1900-01-01"

Output: "11101101100-1-1"

Explanation:

11101101100, 1, and 1 are the binary representations of 1900, 1, and 1 respectively.

'''

class Solution:
    def convertDateToBinary(self, date: str) -> str:
        
        def find(num):
            rem=''
            while num>0:
                rem+=str(num%2)
                num//=2
            return rem[::-1]


        year=date[0:4]
        month=date[5:7]
        date=date[-2:]

        y=find(int(year))
        m=find(int(month))
        d=find(int(date))
        return(f"{y}-{m}-{d}")
        
# Approach 2
class Solution:
    def convertDateToBinary(self, date: str) -> str:
        # Extract year, month, and day from the input string
        year = int(date[:4])
        month = int(date[5:7])
        day = int(date[8:10])
        
        # Convert each part to binary, and strip the '0b' prefix
        y_bin = bin(year)[2:]
        m_bin = bin(month)[2:]
        d_bin = bin(day)[2:]
        
        # Return the formatted binary date as 'year-month-day'
        return f"{y_bin}-{m_bin}-{d_bin}"


  
 
