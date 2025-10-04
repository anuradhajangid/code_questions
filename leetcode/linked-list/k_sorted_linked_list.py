import heapq
from typing import Optional
from typing import List
#https://leetcode.com/problems/merge-k-sorted-lists/

class ListNode:
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKListsBruteForce(self, ksorted: List[Optional[ListNode]]) -> Optional[ListNode]:
        merged = None
        curr = None
        minval = None
        while any(ksorted):
            loc = None
            for i in range(len(ksorted)):
                if not ksorted[i]:
                    continue
                if minval == None:
                    minval = ksorted[i].val
                    pos = ksorted[i]
                    loc = i
                if ksorted[i] and ksorted[i].val <= minval:
                    minval = ksorted[i].val
                    pos = ksorted[i]
                    loc = i
            if not merged:
                curr = pos
                merged = curr
            else:
                curr.next = pos
                curr = curr.next
            ksorted[loc] = pos.next
            curr.next = None
            minval=None
        return merged

    def mergeKListsHead(self, ksorted: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode(None, None)
        curr = head
        h = []
        for i in range(len(ksorted)):
            if ksorted[i]:
                heapq.heappush(h, (ksorted[i].val, i))
                ksorted[i] = ksorted[i].next
        while h:
            val, i = heapq.heappop(h)
            curr.next = ListNode(val)
            curr = curr.next
            if ksorted[i]:
                heapq.heappush(h, (ksorted[i].val, i))
                ksorted[i] = ksorted[i].next
        return head.next

        
inputL = [[0],[1]]
ksorted = []
for list in inputL:
    prev = head = None
    for item in list:
        if not head:
            prev = ListNode(item)
            head = prev
        else:
            prev.next = ListNode(item)
            prev = prev.next
    ksorted.append(head)
s=Solution()
merged = s.mergeKLists(ksorted)
print(merged)


