from typing import Optional

class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            continueHead = head.next
            head.next = prev
            prev = head
            head = continueHead
        return prev
        
prev = None
head = None
for item in [1,2,3,4,5]:
    n = ListNode(item)
    if not prev:
        prev = n
        head = prev
    else:
        prev.next = n
        prev = prev.next

s= Solution()
s.reverseList(head)


