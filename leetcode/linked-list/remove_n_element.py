# Definition for singly-linked list.
#https://leetcode.com/problems/remove-nth-node-from-end-of-list
from typing import List, Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev= slow=fast = head    
        for i in range (n):
            fast = fast.next
            if not fast:
                break
        if not fast:
            return head.next
        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next
        prev.next = slow.next
        return head
            

prev = None
head = None
for item in [1]:
    n = ListNode(item)
    if not prev:
        prev = n
        head = prev
    else:
        prev.next = n
        prev = prev.next

s= Solution()
head = s.removeNthFromEnd(head, 1)
print(head)


