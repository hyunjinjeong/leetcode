class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        # edge [a, b]가 있을 때 a와 b는 인접한 그룹이어야 한다는 뜻이네
        # 특정 node에서 BFS를 돌면서 그룹을 하나씩 증가시키기?
        # 불가능한 경우는 어떻게 감지할까. 노드를 봤을 때 노드가 이미 다른 그룹에 들어가 있으면 불가능한 것으로 보자.
        # 시작은 어떻게 정하지? 그냥 n개 다 해봐야 하나
        # 아 그래프가 나뉘어 있을 수도 있다고 함..!
        def get_group_count(start):
            node_to_group = {start: 1}
            q = collections.deque([(start, 1)])
            max_group = 1

            while q:
                node, group = q.popleft()
                
                max_group = group # 단조 증가하므로..

                for adj in graph[node]:
                    if adj not in node_to_group:
                        node_to_group[adj] = group + 1
                        q.append((adj, group + 1))
                    elif node_to_group[adj] not in (group - 1, group + 1):
                        return -1
            
            return max_group

        graph = [[] for _ in range(n + 1)]
        for start, end in edges:
            graph[start].append(end)
            graph[end].append(start)

        max_counts = []
        visited = set()
        for node in range(1, n + 1):
            if node in visited:
                continue
            
            # group 구하기
            curr_group = {node}
            q = collections.deque([node])
            while q:
                curr = q.popleft()
                for adj in graph[curr]:
                    if adj in curr_group:
                        continue
                    curr_group.add(adj)
                    visited.add(adj)
                    q.append(adj)
            
            print(curr_group)
            
            # 그룹 내에서 모든 노드를 돌면서 최댓값 구하기
            group_max_count = -1
            for curr in curr_group:
                group_count = get_group_count(curr)
                if group_count == -1:
                    return -1
                group_max_count = max(group_max_count, group_count)
            
            max_counts.append(group_max_count)
        
        return sum(max_counts)
