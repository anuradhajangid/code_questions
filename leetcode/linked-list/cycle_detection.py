from typing import Optional
#https://leetcode.com/problems/linked-list-cycle/
class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycleLeastMem(self, head: Optional[ListNode]) -> bool:
        visited = []
        while head:
            if id(head.next) in visited:
                return True
            else:
                visited.append(id(head))
                head = head.next
        return False
    
    def hasCycleLeastRuntime(self, head: Optional[ListNode]) -> bool:
        # Least Runtime
        if not head or not head.next :
            return False
        slow = head
        fast = head.next
        while fast and fast.next:
            if slow == fast:
                return True
            else:
                slow = slow.next
                fast = fast.next.next
        return False
        
prev = None
head = None
mem = None
pos = 1
count = 0
for item in [3,2,0,-4]:
    n = ListNode(item)
    if not prev:
        prev = n
        head = prev
    else:
        prev.next = n
        prev = prev.next
    count += 1
    if pos > 0 and count == pos:
        mem = n
if mem:
    prev.next = mem
s= Solution()
print(s.hasCycleLeastRuntime(head))