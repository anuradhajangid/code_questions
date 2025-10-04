from typing import Optional
from collections import deque

class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        start = end = head
        temp = deque(maxlen=k)
        prev = None
        i = 0
        while True:
            for i in range(k):
                if start:
                    item = start 
                    start = start.next
                    item.next = None
                    temp.append(item)
                else:
                    i -= 1
                    break
            if not prev:
                prev = temp.pop()
                head = prev
            while temp:
                if i == k-1:
                    prev.next = temp.pop()
                    prev = prev.next
                else:
                    prev.next = temp.popleft()
                    prev= prev.next
            if i !=k-1:
                break
        return head
                




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
s.reverseKGroup(head, 3)
print(s)