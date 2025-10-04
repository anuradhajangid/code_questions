#https://leetcode.com/problems/range-sum-of-bst/?envType=problem-list-v2&envId=7p59281
# Definition for a binary tree node.
from typing import Optional
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        sum = 0
        queue = deque()
        queue.append(root)
        while queue:
            node = queue.pop()
            if not node:
                continue
            if low < node.val < high:
                queue.append(node.left)
                queue.append(node.right)
                sum += node.val
                continue
            if node.val >= high:
                queue.append(node.left)
                sum += node.val if node.val == high else 0
                continue
            if node.val <=low:
                queue.append(node.right)
                sum += node.val if node.val == low else 0
        return sum


