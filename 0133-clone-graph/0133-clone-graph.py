"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        dt = {}
        visited = set()

        def dfs(n):
            if not n:
                return
            
            if n.val not in dt:
                dt[n.val] = Node(n.val)
            new_node = dt[n.val]

            visited.add(n.val)
            for neighbor in n.neighbors:
                if neighbor.val not in dt:
                    dt[neighbor.val] = Node(neighbor.val)
                neighbor_node = dt[neighbor.val]
                new_node.neighbors.append(neighbor_node)
                if neighbor.val not in visited:
                    dfs(neighbor)
            
            return new_node
        
        return dfs(node)