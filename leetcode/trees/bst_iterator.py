#https://leetcode.com/problems/binary-search-tree-iterator/
# Definition for a binary tree node.
from collections import deque
from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.traversal = []
        self._bfs(root)
        self.index = 0
        self.root = root

    def _bfs(self,root):
        if root == None:
            return 
        self._bfs(root.left)
        self.traversal.append(root)
        self._bfs(root.right)

    def next(self) -> int:
        node = self.traversal[self.index]
        self.index += 1
        return node.val
    
    def hasNext(self) -> bool:
        return self.index < len(self.traversal)
            
        
    @staticmethod
    def CreateTree(itemList: List) -> TreeNode:
        mystack = deque()
        node = TreeNode(itemList[0])
        head = node
        mystack.append(node)
        count = 2
        position = 1
        while position < len(itemList):
            node = mystack.popleft()
            if itemList[position]:
                node.left = TreeNode(itemList[position])
                mystack.append(node.left)
            position+= 1
            if position < len(itemList):
                if itemList[position]:
                    node.right = TreeNode(itemList[position])
                    mystack.append(node.right)
            position += 1
        return head
    
bSTIterator = BSTIterator(BSTIterator.CreateTree([7, 3, 15, None, None, 9, 20]))
assert bSTIterator.next() == 3
assert bSTIterator.next()== 7
assert bSTIterator.hasNext()== True
assert bSTIterator.next()==9
assert bSTIterator.hasNext()== True
assert bSTIterator.next()==15
assert bSTIterator.hasNext()== True
assert bSTIterator.next()== 20
assert bSTIterator.hasNext()==False
