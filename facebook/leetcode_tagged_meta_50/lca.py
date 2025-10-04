# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/description/?envType=problem-list-v2&envId=7p59281
from collections import defaultdict
from dataclasses import dataclass
from typing import List
import attr



@attr.s
class Node:
    left: int
    right: int
    parent: int
    val: int

    def __eq__(self, other):
        return self.value == other.value


@attr.s
class Tree:
    parent: Node

    def lca_parent(P: Node, Q: Node) -> Node:
        if P == Q:
            return P
        PTrack = P
        QTrack = Q
        while PTrack != QTrack:
            if PTrack != None:
                PTrack = PTrack.parent
            else: 
                PTrack = Q
            if QTrack != None:
                QTrack = QTrack.parent
            else:
                QTrack = P
        return PTrack
        
    def lca_no_parent(P:Node, Q:Node, nodes: List[Node]) ->Node:
        relation = defaultdict()
        for node in nodes:
            if node.left is not None:
                relation[node.left] = node
            if node.right is not None:
                relation[node.right] = node

        PTrack = P
        QTrack = Q
        while P != Q:
            if PTrack in relation:
                PTrack = relation[PTrack]
            else:
                PTrack = Q
            if QTrack in relation:
                QTrack = relation[QTrack]
            else:
                QTrack = P
        return PTrack
            

