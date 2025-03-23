import heapq
from dataclasses import dataclass
from typing import Optional

class Node:
    key: str
    value: str | int | object
    next: Optional['Node'] = None
    prev: Optional['Node'] = None

class Solution:
    def merge_k(self, nums: list[list[Node]]):
        dummy = Node()
        current = dummy
        kMergedHeap = []
        for i, node in enumerate(nums):
            if node:
                heapq.heappush(kMergedHeap, (node.value, i, node))

        while kMergedHeap:
            _, i, node = heapq.heappop(kMergedHeap)
            current.next = node
            current = current.next

            if node.next:
                heapq.heappush(kMergedHeap, (node.next.value, i, node.next))
        return dummy.next
    
