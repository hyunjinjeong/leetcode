"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return

        dt = {node.val: Node(node.val)}
        self.dfs(node, dt)
        return dt[node.val]
    
    def dfs(self, old_node, dt):
        new_node = dt[old_node.val]

        for old_neighbor in old_node.neighbors:
            if old_neighbor.val not in dt:
                dt[old_neighbor.val] = Node(old_neighbor.val)
                new_node.neighbors.append(dt[old_neighbor.val])
                self.dfs(old_neighbor, dt)
            else:
                new_node.neighbors.append(dt[old_neighbor.val])