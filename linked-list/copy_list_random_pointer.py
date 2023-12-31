# Definition for singly-linked list.
#https://leetcode.com/problems/copy-list-with-random-pointer
from typing import List, Optional
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hash = {None: None}
        current = head
        
        while current:
            hash[current] = Node(current.val)
            current = current.next
            
        current = head
        
        while current:
            copy = hash[current]
            copy.next = hash[current.next]
            copy.random = hash[current.random]
            current = current.next
            
        return hash[head]


        
            
head = prev = None
nummap = {}
counter = 0
for [number, pointer] in [[3,None],[3,0],[3,None]]:
    n = Node(number, None, pointer)
    nummap[counter] = n
    if prev:
        prev.next = n
        prev = prev.next
    else:
        prev = n
        head = prev
    counter += 1
prev = head
for [number, pointer] in [[3,None],[3,0],[3,None]]:
    if pointer != None:
        prev.random = nummap[pointer]
    prev = prev.next

s= Solution()
copy = s.copyRandomList(head)
print(head)


