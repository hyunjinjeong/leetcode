class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        # graph 문제인가?
        # graph를 그릴 수 있고.. topology sort 느낌인데
        # in_degree가 0개인 거에서 시작해서 DFS 돌리면 되려나?
        # 일단 처음엔 in_node가 0인 노드가 1개 있어야 함. 그 뒤로는 모두 1이어야 하고
        root = 0
        children_nodes = set(leftChild + rightChild)
        for i in range(n):
            if i not in children_nodes:
                root = i
                break
        
        q = collections.deque([root])
        visited = set()
        
        while q:
            node = q.popleft()
            if node in visited:
                return False
            visited.add(node)
            
            if leftChild[node] != -1:
                q.append(leftChild[node])
            if rightChild[node] != -1:
                q.append(rightChild[node])
        
        return len(visited) == n
        
        