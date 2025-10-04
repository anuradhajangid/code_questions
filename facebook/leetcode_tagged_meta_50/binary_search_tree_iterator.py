#https://leetcode.com/problems/binary-search-tree-iterator/?envType=problem-list-v2&envId=7p59281
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.iterator = []
        self.position = 0
        def dfs(node:TreeNode):
            if not node:
                return 
            dfs(node.left)
            self.iterator.append(node.val)
            dfs(node.right)
        current = root
        dfs(current)
        print(self.iterator)

    def next(self) -> int:
        value = None
        if self.position >= len(self.iterator):
            return None
        else:
            value = self.iterator[self.position]
            self.position += 1
        return value
        

    def hasNext(self) -> bool:
        return self.position < len(self.iterator)
