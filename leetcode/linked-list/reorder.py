# Definition for singly-linked list.
#https://leetcode.com/problems/reorder-list/
from typing import List, Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderListLeastMem(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        running = start = head
        while start:
            pre = running = start
            while running.next:
                pre = running
                running = running.next 
            if pre != start:
                pre.next = None
                temp = start.next
                start.next = running
                start.next.next = temp
                start = start.next.next
            else:
                start = start.next
        
    def reorderListLeastRuntime(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #Find the mid of list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #Reverse the list after mid
        head2 = slow.next
        slow.next = None

        moving = head2
        prev = None
        while moving:
            temp = moving.next
            moving.next = prev
            prev = moving
            moving = temp

        #Merge the two lists
        original, updated = head, prev
        while updated:
            tempo, tempu = original.next, updated.next
            original.next, updated.next  = updated, tempo
            original, updated = tempo, tempu






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
s.reorderListLeastRuntime(head)