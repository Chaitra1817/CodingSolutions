'''

Given the head of a singly linked list, the task is to find the starting point of a loop in the linked list if it exists. Return the starting node if a loop exists; otherwise, return null.


A loop exists in a linked list if some node in the list can be reached again by continuously following the next pointer. Internally, pos denotes the index (0-based) of the node from where the loop starts.


Note that pos is not passed as a parameter.

Input: head -> 1 -> 2 -> 3 -> 4 -> 5, pos = 1

Output(value of the returned node is displayed): 2

Expla﻿nation: The tail of the linked list connects to the node at 1st index.

'''

# Definition of singly linked list:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def findStartingPoint(self, head):
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                break
        else:
            return None
            
        slow=head
        while slow!=fast:
            slow=slow.next
            fast=fast.next
        return slow

