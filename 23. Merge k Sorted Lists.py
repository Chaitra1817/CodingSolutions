'''
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted linked list:
1->1->2->3->4->4->5->6

Example 2:

Input: lists = []
Output: []

Example 3:

Input: lists = [[]]
Output: []

 

Constraints:

    k == lists.length
    0 <= k <= 104

'''

#Approach1

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import List, Optional

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = None

        def merge(a, b):
            if not a:
                return b
            if not b:
                return a
            
            if a.val>b.val:
                a,b=b,a

            prev = None
            cur = a  

            while a and b:
                if a.val <= b.val:
                    prev = a
                    a = a.next
                else:
                    temp = b.next
                    prev.next = b
                    b.next = a
                    prev = b
                    b = temp

            if b:
                prev.next = b

            return cur

        for item in lists:
            head = merge(head, item)
        return head
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import List, Optional

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        hp=[]
        for idx,node in enumerate(lists):
            if node:
                heapq.heappush(hp,(node.val,idx,node))
        
        dummy=ListNode(-1,None)
        cur=dummy
        while hp:
            val,idx,node=heapq.heappop(hp)
            cur.next=node
            cur=cur.next
            if node.next:
                heapq.heappush(hp,(node.next.val,idx,node.next))
        
        return dummy.next


        


