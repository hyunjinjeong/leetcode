"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # 3가지 방법: 1. Recursive DFS, 2. Iterative DFS, 3. Iterative BFS 가능. 난 1번이 젤 쉽당.
        # 다른 것도 알아는 두자...
        if not node:
            return None
        
        new_node = Node(node.val)
        dt = {node: new_node} # 일종의 visited 역할도 함.
        
        def dfs(n):
            for neighbor in n.neighbors:
                if neighbor not in dt:
                    new_neighbor_node = Node(neighbor.val)
                    dt[neighbor] = new_neighbor_node
                    dt[n].neighbors.append(new_neighbor_node)
                    dfs(neighbor)
                else:
                    dt[n].neighbors.append(dt[neighbor])
        
        dfs(node)
        
        return new_node