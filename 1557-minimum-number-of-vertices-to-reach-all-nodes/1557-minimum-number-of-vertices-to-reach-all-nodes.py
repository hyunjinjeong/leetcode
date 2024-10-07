class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        # union find...는 적용하기 애매하고
        # topological sort인가? 그냥 in degree가 0인 것들 모으면 되는거 같은데
        in_degree = [0] * n

        for u, v in edges:
            in_degree[v] += 1
        
        res = []
        for node in range(n):
            if in_degree[node] == 0:
                res.append(node)
        
        return res