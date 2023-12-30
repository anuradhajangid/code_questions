from typing import Optional

class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        mergedhead = interim = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                interim.next = list1
                list1 = list1.next
                interim = list1
            else:
                interim.next = list2
                list2 = list2.next
                interim = list2
        if list1 or list2:
            interim.next = list1 if list1 else list2

        return mergedhead.next
        


head1 = None
head2 = None 
for head, nums in zip([head1,head2], [[1,2,4], [1,3,4]]):
    prev = None
    for item in nums:
        n = ListNode(item)
        if not prev:
            prev = n
            head = prev
        else:
            prev.next = n
            prev = prev.next
    if not head1:
        head1 = head
    else:
        head2 = head 

s= Solution()
s.mergeTwoLists(head1, head2)


