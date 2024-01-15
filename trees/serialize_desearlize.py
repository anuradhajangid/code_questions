from collections import deque
from typing import List, Optional
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/
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
        position = 1
        while position < len(input):
            node = mystack.popleft()
            if position < len(input):
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
            

    def insert(self, node:TreeNode, value):
        if node is None:
            return self._createNode(value)
        if value < node.val:
            node.left = self.insert(node.left, value)
        elif value > node.val:
            node.right = self.insert(node.right, value)
        else:
            raise TypeError("Repeated value in tree not allowed")
        return node
    
    def searchBF(self, node: TreeNode, searchvalue):
        if node is None or node.val == searchvalue:
            return node
        
        if searchvalue < node.val:
            return self.search(node.left, searchvalue)
        else:
            return self.search(node.right, searchvalue)
    
    def searchDF(self, node: TreeNode, searchValue):
        queue = []

        if node is None:
            return None
        
        queue.append(node)

        while queue:
            temp = queue.pop()
            if temp.val == searchValue:
                return temp
            if temp.left is not None:
                queue.append(temp.left)
            if temp.right is not None:
                queue.append(temp.right)

        
    def delete(self, node, delvalue):
        if node is None:
            return None
        
        if delvalue < node.left:
            self.delete(node.left, delvalue)
        elif delvalue > node.right:
            self.delete(node, node.right)
        else:
            if node.left is None and node.right is None:
                del node
                return None
            else :
                templ = node.left
                tempr = node.right
                del node
                return [templ, tempr]
    
    def traverseInOrder(self, node):
        if node is not None:
            self.traverseInOrder(node.left)
            print(node.value)
            self.traverseInOrder(node.right)

    def traversePreOrder(self, node):
        if node is not None:
            print(node.val)
            self.traversePreOrder(node.left)
            self.traversePreOrder(node.right)
    
    def traversePostOrder(self, node):
        if node is not None:
            self.traversePostOrder(node.left)
            self.traversePostOrder(node.right)
            print(node.val)
        

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        output = ""
        current = deque()
        current.append(root)
        while current:
            item = current.popleft()
            if item:
                output+=f"{item.val}," 
            else:
                output+= "$,"
            if item is not None:
                current.append(item.left)
                current.append(item.right)
        return output

        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if(len(data)==0):
            return None
        inputdata = data.split(",")
        if(inputdata[0]=="$"):
            return None
        mystack = deque()
        inputdata.pop()
        node = TreeNode(int(inputdata[0]))
        head = node
        mystack.append(node)
        position = 1

        while position < len(inputdata):
            node = mystack.popleft()
            if inputdata[position]:
                if inputdata[position] == "$":
                    node.left = None
                else:
                    node.left = TreeNode(inputdata[position])
                    mystack.append(node.left)
            position+= 1
            if position < len(inputdata):
                if inputdata[position] == "$":
                    node.right = None
                else:
                    node.right = TreeNode(inputdata[position])
                    mystack.append(node.right)
            position += 1
        return head
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))


        

tr = Tree()
head = None
input = [1,2,3,None,None,4,5]
head = tr.create(head, input)

s = Codec()
print(s.deserialize(s.serialize(head)))