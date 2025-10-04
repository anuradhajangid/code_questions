from typing import Optional
#https://leetcode.com/problems/add-two-numbers/
class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        count = 1
        head = None
        prev = None
        carry = 0
        while l1 or l2:
            n1, n2= 0,0
            if l1:
                n1 = l1.val
                l1 = l1.next
            if l2:
                n2 = l2.val
                l2 = l2.next
            nodeval, carry = (n1 + n2 + carry)%10, (n1 + n2 + carry)//10
            n = ListNode(nodeval)
            if prev == None:
                prev = n
                head = prev
            else:
                prev.next = n
                prev = prev.next
        if carry:
            n = ListNode(carry)
            prev.next = n
        return head




linkedlists = []
for list in [[2,4,3], [5,6,4]]:
    prev = None
    head = None
    for item in list:
        n = ListNode(item)
        if not prev:
            prev = n
            head = prev
        else:
            prev.next = n
            prev = prev.next
    linkedlists.append(head)
s= Solution()
s.addTwoNumbers(*linkedlists)