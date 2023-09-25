#https://leetcode.com/problems/min-stack/submissions/
class Node:
    def __init__(self, value):
        self.value = value
        self.minvalue = None
        self.bottom = None

class MinStack:

    def __init__(self):
        self.node = None

    def push(self, val: int) -> None:
        newNode = Node(val)
        if not self.node:
            newNode.minvalue = val
            self.node = newNode
        else:
            newNode.bottom = self.node
            newNode.minvalue = val if self.node.minvalue > val else self.node.minvalue
            self.node = newNode
        

    def pop(self) -> None:
        self.node = self.node.bottom
        

    def top(self) -> int:
        return self.node.value
        

    def getMin(self) -> int:
        return self.node.minvalue
            

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()