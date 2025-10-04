from datetime import datetime
from collections import defaultdict
from typing import Dict
class Node:
    def __init__(self, key:str, value:object, ttl:int) -> None:
        self.next = None
        self.prev = None
        self.key = key
        self.value = value
        self.ttl = ttl
        self.expireAt = datetime.now() + ttl
    
    def refresh(self):
        self.expireAt = datetime.now() + self.ttl

    def update(self, value, ttl: None):
        self.value = value
        self.ttl = ttl if ttl else self.ttl
        self.expireAt = datetime.now() + self.ttl

class LRUCache:
    def __init__(self, capacity: int = 1000, ttl: int = 10):
        self.ttlDefault = ttl
        self.capacity = capacity
        self.head = Node("", "")
        self.tail = Node("", "")
        self.map: Dict[str, Node] = defaultdict()
        self.head.prev = self.tail
        self.tail.next = self.head

    def _move_to_front(self, node:Node) -> None:
        node.prev.next, node.next.prev = node.next, node.prev
        node.prev = self.head.prev
        self.head.prev.next = node
        self.head.prev = node
        node.refresh()
        return

    def _clean_last(self) -> None:
        node = self.tail.next
        self.tail.next, self.tail.next.next.prev = self.tail.next.next, self.tail
        del self.map[node.key]
        del node
        return 
    
    def _add_to_front(self, node:Node) -> None:
        node.prev = self.head.prev
        node.next = self.head
        self.head.prev = node
        return
    
    def _remove_expired(self, timenow):
        expired_keys = [(key, value) for key, value in self.map.items() if value.expiredAt < timenow]
        for key, node in expired_keys:
            node.prev.next, node.next.prev = node.next, node.prev
            del node
            del self.map[key]
        return
        
    def get(self, key: str, timenow: datetime = datetime.now()) -> object | None:
        self._remove_expired(timenow)
        if key in self.map:
            self._move_to_front(self.map[key], timenow)
            return self.map[key].value
        return -1


    def put(self, key: str, value: str | int | object, ttl: int = None, timenow: datetime = datetime.now()) -> None:
        self._remove_expired(timenow)
        if key in self.map:
            self.map[key].update(value, ttl)
            self._move_to_front(self.map[key])
        else:
            if self.capacity <= len(self.map):
                self._clean_last()
            self._add_to_front(Node(key, value, ttl))
        return

