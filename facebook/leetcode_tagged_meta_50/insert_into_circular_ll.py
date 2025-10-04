#https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/description/?envType=problem-list-v2&envId=7p59281
from dataclasses import dataclass


@dataclass
class Node:
    val: int
    next: int
class Solution:
    def insertCircularLL(node:Node, insertVal:int):
        original = node
        insertVal = Node(insertVal)
        if not node:
            insertVal.next = insertVal
            return insertVal
        while node.next is not original:
            if insertVal.val >= node.val:
                if insertVal < node.next.val or node.val > node.next.val:
                    insertVal.next = node.next
                    node.next = insertVal
                    return
                else:
                    node = node.next
        return original


