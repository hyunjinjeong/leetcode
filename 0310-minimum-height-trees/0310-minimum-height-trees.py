class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # 오.. 어렵다
        # 1. dfs 2번 활용: diameter를 찾아서 중간의 노드들을 리턴하는 방법도 있고, (leaf 하나 찾고 거기서 반대편 leaf를 찾으면 됨)
        # 2. bfs 활용: leaves를 순서대로 제거해서 루트를 찾는 방법도 있음.
        # MHT가 최대 2개라는 사실 이용.
        # bfs 방법은 topological sort를 거꾸로 하는 것과 비슷..
        
        # 1. dfs 버전
        graph, seen = collections.defaultdict(set), [False] * n
        # 초기화
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        
        def dfs(i):
            if seen[i]:
                return []
            
            longest_path = []
            seen[i] = True
            for adj in graph[i]:
                if seen[adj]:
                    continue
                path = dfs(adj)
                if len(path) > len(longest_path):
                    longest_path = path
            
            longest_path.append(i)
            seen[i] = False
            return longest_path
        
        # 하나는 랜덤하게 골라서 끝에 있는 원소를 찾고
        edge = dfs(0)[0]
        # 끝에 있는 원소로부터 dfs 실행하면 diameter가 됨.
        path = dfs(edge)
        # 길이가 짝수면 2개, 홀수면 1개
        return [path[len(path)//2], path[len(path)//2 - 1]] if len(path) % 2 == 0 else [path[len(path)//2]]