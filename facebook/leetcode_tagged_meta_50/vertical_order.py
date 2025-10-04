# Definition for a binary tree node
from typing import List
from collections import defaultdict, deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        data = defaultdict(list)
        queue = deque()
        if not root:
            return []
        queue.append((root, 0, 0))
        pre_row = 0
        while queue:
            node, col, row = queue.pop()
            data[col].append((node.val, row))
            if node.left: 
                queue.append((node.left, col-1, row+1)) 
            if node.right: 
                queue.append((node.right, col+1, row+1))
        keys = sorted(data.keys())
        result = []
        for key in keys:
            value = data[key]
            value.sort(key=lambda x: (x[1],x[0]))
            result.append([v for v,_ in value])
        return result
    

"""
Example:
Input: root = [3,9,20,null,null,15,7]
Output: [[9],[3,15],[20],[7]]
data = {
    0: [3,15]
    -1: [9]
    1: [20]
    2: [7]
}
queue = ()
keys = -1,0,1,2
result = [[9],[3,15],[20],[7]]
"""
            
