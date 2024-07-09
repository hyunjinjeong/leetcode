class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        # graph 문제인가?
        # graph를 그릴 수 있고.. topology sort 느낌인데
        # in_degree가 0개인 거에서 시작해서 DFS 돌리면 되려나?
        # 일단 처음엔 in_node가 0인 노드가 1개 있어야 함. 그 뒤로는 모두 1이어야 하고
        graph = {i:set() for i in range(n)}
        in_degree = {i:0 for i in range(n)}
        for u, v in enumerate(leftChild):
            if v != -1:
                graph[u].add(v)
                in_degree[v] += 1
        for u, v in enumerate(rightChild):
            if v != -1:
                graph[u].add(v)
                in_degree[v] += 1
        
        q = collections.deque()
        for node in in_degree:
            if in_degree[node] == 0:
                q.append(node)
        
        if len(q) != 1:
            return False
        
        visited = 0
        while q:
            node = q.popleft()
            visited += 1
            for child in graph[node]:
                in_degree[child] -= 1
                if in_degree[child] != 0:
                    return False
                q.append(child)
        
        return visited == n
        
        