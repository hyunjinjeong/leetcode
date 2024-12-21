class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # 일단 위상 정렬인데
        # brute force라면 queries[i] = [u, v]라면 u에서 시작해서 v로 가는 도착지가 있는 경우를 매번 구해야 함
        # 근데 노드가 최대 100개니까 이것도 그렇게 오래 걸리지는 않을 거임. 일단 이렇게 해보자...

        # 여기서 최적화를 하려면 결과를 계산해야 해서 어딘가에 저장을 해둬야 할듯?
        def dfs(node):
            if node not in can_reach:
                can_reach[node] = set([node])
                for nei in graph[node]:
                    can_reach[node].update(dfs(nei))
            return can_reach[node]

        graph = {i: [] for i in range(numCourses)}
        for start, end in prerequisites:
            graph[start].append(end)
        
        can_reach = {}
        for node in range(numCourses):
            dfs(node)
        
        res = []
        for start, end in queries:
            res.append(end in can_reach[start])
        return res