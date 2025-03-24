import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__),'../../'))
from hello_interview.tree import Tree

class Solution:
    def pathSum(self, root, target):
        if not root:
            return False
        if not root.left and not root.right:
            return root.value == target
        if self.pathSum(root.left, target - root.value) or self.pathSum(root.right, target - root.value):
            return True
        return False



tree = Tree().createTree([4, 2, 7, 1, None, 6, 9, None, 8, None, None, None, None, None, None])

assert Solution().pathSum(tree, 15) == True