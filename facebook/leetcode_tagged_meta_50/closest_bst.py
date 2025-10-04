#https://events.sulekha.com/sef-dandia-2025_event-in_santa-clara-ca_393392
from typing import Optional
from math import inf

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        """
        Find the value in a BST that is closest to the target.
        If there are multiple values with the same difference, return the smaller value.
      
        Args:
            root: Root node of the binary search tree
            target: Target value to find the closest node value to
          
        Returns:
            The closest integer value in the BST to the target
        """
        found_node = None
        min_diff = float(inf)
        def dfs(node):
            nonlocal found_node, min_diff
            if not node:
                return 
            diff = abs(node.val - target.val)
            if  diff < min_diff:
                min_diff = diff
                found_node = node
            if target < node.val:
                dfs(node.left)
            else:
                dfs(node.right)
        
        dfs(root)
        return min_diff