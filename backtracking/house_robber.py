#https://www.educative.io/courses/grokking-coding-interview-patterns-python/house-robber-iii
from typing import List
from queue import Queue
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, nodes):
        self.root = self.createBinaryTree(nodes)

    def createBinaryTree(self, nodes):
        if len(nodes) == 0:
            return None

        # Create the root node of the binary tree
        root = TreeNode(nodes[0].data)

        # Create a queue and add the root node to it
        queue = Queue()
        queue.put(root)

        # Start iterating over the list of nodes starting from the second node
        i = 1
        while i < len(nodes):
            # Get the next node from the queue
            curr = queue.get()

            # If the node is not None, create a new TreeNode object for its left child,
            # set it as the left child of the current node, and add it to the queue
            if nodes[i] is not None:
                curr.left = TreeNode(nodes[i].data)
                queue.put(curr.left)

            i += 1

            # If there are more nodes in the list and the next node is not None,
            # create a new TreeNode object for its right child, set it as the right child
            # of the current node, and add it to the queue
            if i < len(nodes) and nodes[i] is not None:
                curr.right = TreeNode(nodes[i].data)
                queue.put(curr.right)

            i += 1

        # Return the root of the binary tree
        return root


def rob(root):
   return max(heist(root))
   
def heist(root):
    if root == None: 
        return [0, 0]

    left_subtree = heist(root.left) 
    right_subtree  = heist(root.right)
    include_root = root.data + left_subtree[1] + right_subtree[1] 
    exclude_root = max(left_subtree) + max(right_subtree)

    return [include_root, exclude_root] 

if __name__ == '__main__':
    
    # Create a list of list of TreeNode objects to represent binary trees
    list_of_trees = [ [TreeNode(10), TreeNode(9), TreeNode(20), TreeNode(15), TreeNode(7)],
                    [TreeNode(7), TreeNode(9), TreeNode(10), TreeNode(15), TreeNode(20)],
                    [TreeNode(8), TreeNode(2), TreeNode(17), TreeNode(1), TreeNode(4), TreeNode(19), TreeNode(5)],
                    [TreeNode(7), TreeNode(3), TreeNode(4), TreeNode(1), TreeNode(3)],
                    [TreeNode(9), TreeNode(5), TreeNode(7), TreeNode(1), TreeNode(3)],
                    [TreeNode(9), TreeNode(7), None, None, TreeNode(1), TreeNode(8), TreeNode(10), None, TreeNode(12)]
    ]

    # Create the binary trees using the BinaryTree class
    input_trees = []
    for list_of_nodes in list_of_trees:
        tree = BinaryTree(list_of_nodes)
        input_trees.append(tree)

    # Print the input trees
    x = 1
    for tree in input_trees:
        print(x, ".\tInput Tree:", sep = "")
        x += 1
        print("\tMaximum amount we can rob without getting caught: ", rob(tree.root), sep = "")
        print("-" * 100)
