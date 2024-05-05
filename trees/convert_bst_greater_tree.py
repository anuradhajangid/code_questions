#https://leetcode.com/problems/convert-bst-to-greater-tree/
from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self, map) -> None:
        node = TreeNode(map[0])
        self.map = node
        queue = deque()
        queue.append(node)
        count = 0
        while queue and count < len(map):
            temp = queue.popleft()
            count += 1
            if count < len(map) and map[count] != None:
                node = TreeNode(map[count])
                temp.left = node
                queue.append(node)
            count += 1
            if count < len(map) and map[count] != None:
                node = TreeNode(map[count])
                temp.right = node
                queue.append(node)

    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node, val):
            if node.right:
                val = dfs(node.right, val)
            val += node.val
            node.val = val
            if node.left:
                val = dfs(node.left, val)
            return val
        if not self.map:
            return self.map
        dfs(self.map, 0)
        return 


#assert  Solution([4,1,6,0,2,5,7,None,None,None,3,None,None,None,8]).convertBST([4,1,6,0,2,5,7,None,None,None,3,None,None,None,8]) #== [30,36,21,36,35,26,15,None,None,None,33,None,None,None,8]
assert Solution([0,None,1]).convertBST([0,None,1]) #== [1,None,1]
