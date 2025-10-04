#https://leetcode.com/problems/binary-tree-right-side-view/description/?envType=problem-list-v2&envId=7p59281
# Definition for a binary tree node.
from typing import Optional, List
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        right = []
        queue = deque()
        pre_count = 0
        if root:
            queue.append((0, root))
        while queue:
            count, node = queue.pop()
            if count == pre_count:
                right.append(node.val)
                pre_count += 1
            if node.right:
                queue.append((count +1, node.right))
            if node.left:
                queue.append((count + 1, node.left))
        return right
        
