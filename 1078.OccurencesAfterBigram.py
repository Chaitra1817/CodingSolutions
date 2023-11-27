'''
1078. Occurrences After Bigram
Solved
Easy
Topics
Companies
Hint

Given two strings first and second, consider occurrences in some text of the form "first second third", where second comes immediately after first, and third comes immediately after second.

Return an array of all the words third for each occurrence of "first second third".

 

Example 1:

Input: text = "alice is a good girl she is a good student", first = "a", second = "good"
Output: ["girl","student"]

Example 2:

Input: text = "we will we will rock you", first = "we", second = "will"
Output: ["we","rock"]

'''
class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        temp=text.split()
        ans=[]
        for i in range(len(temp)-2):
            if temp[i]+temp[i+1]==first+second:
                ans.append(temp[i+2])
        return ans

        
