# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        running = head.next
        head.next = None
        if not head:
            return []
        while running:
            temp = running
            running = running.next
            temp.next = None
            if temp.val <= head.val:
                head, temp.next = temp, head
            else:
                next = head.next
                previous = head
                while next:
                    if temp.val <= next.val and temp.val >= previous.val:
                        previous.next = temp
                        temp.next= next
                        break
                    previous = next
                    next = next.next
                if not next and temp.val > previous.val:
                    previous.next = temp
                    temp.next = None
        return Solution.ReturnArray(head)
    
    @staticmethod
    def ReturnArray(head:Optional[ListNode]):
        result = []
        while head:
            result.append(head.val)
            head = head.next
        return result

        
        
    @staticmethod   
    def ConstructLL(ll):
        current, head = None, None
        for item in ll:
            node = ListNode(item)
            if not head:
                head = node
                current = node
                continue
            current.next= node
            current = current.next
        return head

assert Solution().insertionSortList(Solution.ConstructLL([4,2,1,3])) == [1,2,3,4]
assert Solution().insertionSortList(Solution.ConstructLL([-1,5,3,4,0])) == [-1,0,3,4,5]