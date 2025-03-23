from dataclasses import dataclass
from typing import Optional
class Node:
    key: str
    value: str | int | object
    next: Optional['Node'] = None
    prev: Optional['Node'] = None

class LRUCache:
    def __init__(self, capacity:int):
        self.capacity = capacity
        self._map = {}
        self.head = None
        self.tail = None

    def _remove(self,key):
        lru = self._map[key]
        lru.pre.next = lru.next
        del self._map[key]

    def _add(self, node: Node) -> None:
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.next, self.head.prev = self.head, node
            self.head = node
        self._map[node.key] = node

    def get(self, key:str):
        if key in self._map:
            node = self._map[key]
            self._remove(node)
            self._add(node)
        else:
            return None
    
    def put(self, key, value):
        node = Node(key,value)
        if len(self._map) >= self.capacity:
            node = self.tail
            self._remove(node)
            del self._map[key]
            del node
        self._add(node)
        