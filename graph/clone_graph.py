
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        newNode = Node(node.val)
        nodes = {node.val:newNode}
        def helper(neighbors, newNode, nodes):
            for neighbor in neighbors:
                if neighbor.val not in nodes:
                    node = Node(neighbor.val)
                    newNode.neighbors.append(node)
                    nodes[neighbor.val] = node
                    helper(neighbor.neighbors, node, nodes)
                else:
                    if len(newNode.neighbors) != neighbors and neighbor not in newNode.neighbors:
                        newNode.neighbors.append(nodes[neighbor.val])
        helper(node.neighbors, newNode, nodes)
        return newNode
#[[2,4],[1,3],[2,4],[1,3]]
nodes = [Node(1),Node(2),Node(3),Node(4)]
nodes[0].neighbors.extend([nodes[1],nodes[3]])
nodes[1].neighbors.extend([nodes[0], nodes[2]])
nodes[2].neighbors.extend([nodes[1], nodes[3]])
nodes[3].neighbors.extend([nodes[0], nodes[2]])

s = Solution()
new = s.cloneGraph(nodes[0])
assert nodes[0].val == new.val
assert nodes[0].neighbors[0].val == new.neighbors[0].val
assert nodes[0].neighbors[1].val == new.neighbors[1].val


    