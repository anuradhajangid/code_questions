import dataclasses
from typing import Any, Dict

@dataclasses
class Node:
    key: int
    val: int
    next: int = None
    prev: int = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map: Dict = dict()
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _remove(self,node:Node) -> None:
        node.prev.next, node.next.prev = node.next.prev, node.prev.next
        return

    
    def _add(self,node:Node) -> None:
        if len(self.map) > self.capacity:
            node = self.tail.prev
            self.tail.prev = node.prev
            del node
            del self.map[node.key]
        self.head.next.prev, node.next = node, self.head.next
        self.head.next = node



    def get(self, key: int) -> int:
        if key in self.map:
            node = self.map(key)
            self._remove(node)
            self._add(node)
            return node.value
        return -1

        

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            self._remove(node)
            del node
        node = Node(key, value)
        self.map[key] = node
        self._add(node)
        return 
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)