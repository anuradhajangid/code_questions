#https://leetcode.com/problems/copy-list-with-random-pointer/description/?envType=problem-list-v2&envId=7p59281

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

from typing import Optional
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        map = dict()
        map[None] = None

        current = head
        while current:
            map[current] = Node(current.val)
            current = current.next
        
        current=head

        while current:
            copy = map[current]
            copy.next = map[current.next]
            copy.random = map[current.random]
            current = current.next
        
        return map[head]