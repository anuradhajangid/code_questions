from typing import List
from collections import deque
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None
    def createTree(self, values: List):
        if not values:
            return None
        self.root = Node(values[0])
        queue = deque()
        queue.append(self.root)
        index = 1
        while index < len(values):
            current = queue.popleft()
            if values[index] is not None:
                current.left = Node(values[index])
                queue.append(current.left)
            index += 1
            if index < len(values) and values[index] is not None:
                current.right = Node(values[index])
                queue.append(current.right)
            index+=1
        return self.root
            

Tree().createTree([4, 2, 7, 1, None, 6, 9, None, 8, None, None, None, None, None, None])