#https://leetcode.com/problems/lru-cache/
class Node:
    def __init__(self, key, value) -> None:
        self.next = None
        self.prev = None
        self.key = key
        self.value = value
class LRUCache:

    def __init__(self, capacity: int):
        self.head = None
        self.tail = None
        self.head = Node(0, 0)
        self.tail = Node(-1, -1)
        self.capacity = capacity
        self.map = {}
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def get(self, key: int) -> int:
        if key in self.map:
            node = self.map[key]
            self._deleteNode(node)
            self._addNode(node)
            return node.value
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node  = self.map[key]
            self._deleteNode(node)
            self._addNode(node)
            node.value = value
        else:
            if len(self.map) >= self.capacity:
                self._popNode()
            node = Node(key, value)
            self._addNode(node)
            self.map[key] = node
        

    def _deleteNode(self, node:Node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _addNode(self, node):
        headNext = self.head.next 
        self.head.next = node 
        node.prev = self.head 
        node.next = headNext 
        headNext.prev = node

    def _popNode(self):
        if len(self.map) == 0: return
        tail_node = self.tail.prev
        del self.map[tail_node.key]
        self._deleteNode(tail_node)






        
        


# Your LRUCache object will be instantiated and called as such:
capacity = 2
obj = LRUCache(capacity)
for function, value in zip(["put","put","get","put","get","put","get","get","get"], [[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]):
    if function == "put":
        fun  = obj.put
    else:
        fun = obj.get

    fun(*value)