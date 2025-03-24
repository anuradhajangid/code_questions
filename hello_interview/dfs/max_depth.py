import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__),'../../'))
from hello_interview.tree import Tree

class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1



tree = Tree().createTree([4, 2, 7, 1, None, 6, 9, None, 8, None, None, None, None, None, None])

assert Solution().maxDepth(tree) == 4