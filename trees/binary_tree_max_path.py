# https://leetcode.com/problems/binary-tree-maximum-path-sum/

from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Tree:
    def _createNode(self, value):
        return TreeNode(value)

    def create(self, head, input):
        mystack = deque()
        node = TreeNode(input[0])
        head = node
        mystack.append(node)
        count = 2
        position = 1
        while position < len(input):
            node = mystack.popleft()
            if input[position]:
                node.left = TreeNode(input[position])
                mystack.append(node.left)
            position+= 1
            if position < len(input):
                if input[position]:
                    node.right = TreeNode(input[position])
                    mystack.append(node.right)
            position += 1
        return head

class Solution:
    def maxPathSum(root: Optional[TreeNode]) -> int:
        max_path = float("-inf")
        def bfs_max(node):
            nonlocal max_path
            if node == None:
                return 0
            left_max = max(bfs_max(node.left), 0)
            right_max = max(bfs_max(node.right), 0)
            this_path_max = node.val + left_max + right_max
            max_path = max(max_path, this_path_max)
            return node.val + max(left_max, right_max)
        bfs_max(root)
        return max_path
        

tr = Tree()
head = None
input = [-10,9,20,None,None,15,7]
head = tr.create(head, input)
print(Solution.maxPathSum(head))