'''
Given the head of a singly linked list, return true if it is a

or false otherwise.

 

Example 1:

Input: head = [1,2,2,1]
Output: true

Example 2:

Input: head = [1,2]
Output: false

 

Constraints:

    The number of nodes in the list is in the range [1, 105].
    0 <= Node.val <= 9

 
Follow up: Could you do it in O(n) time and O(1) space?

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack=[]
        while head:
            stack.append(head.val)
            head=head.next
        
        left=0
        right=len(stack)-1

        while left<right:
            if stack[left]!=stack[right]:
                return False
            left+=1
            right-=1
        return True

'''

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow=head
        fast=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        
        mid=None
        while slow:
            temp=slow.next
            slow.next=mid
            mid=slow
            slow=temp
        
        first,second=head,mid
        while second:
            if first.val!=second.val:
                return False
            first=first.next
            second=second.next
        return True


