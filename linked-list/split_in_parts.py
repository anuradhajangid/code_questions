#https://leetcode.com/problems/split-linked-list-in-parts/description/
# Definition for singly-linked list
from typing import Optional, List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def __init__(self, ll) -> None:
        head = None
        currentNode = None
        for item in ll:
            node = ListNode(item)
            if not head:
                head = node
                currentNode = node
            currentNode.next = node
            currentNode = node
        self.head = head

    def splitListToParts(self, k: int) -> List[Optional[ListNode]]:
        p1 = self.head
        p2 = self.head
        count = 0
        p2count  = 0
        while p2:
            for p2count in  range(k):
                p2 = p2.next
                if not p2:
                    break
            if p2count == k-1:
                count += 1
            else:
                break
        result = []
        p2count += 1
        p = self.head        
        for _ in range(k):
            temp = []
            if count: 
                for _ in range(count):
                    temp.append(p.val)
                    p = p.next
            if p2count:
                temp.append(p.val)
                p = p.next
                p2count -= 1
            result.append(temp)
        return result
        


assert Solution([1,2,3]).splitListToParts(k = 5) == [[1],[2],[3],[],[]]
assert Solution([1,2,3,4,5,6,7,8,9,10]).splitListToParts(k = 3) == [[1,2,3,4],[5,6,7],[8,9,10]]
