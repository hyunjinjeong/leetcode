class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # 일단 위상 정렬인데
        # 한번 돌고 끝이 아니라 쿼리마다 결과를 계산해야 해서 어딘가에 저장을 해둬야 할듯?
        # brute force라면 queries[i] = [u, v]라면 u에서 시작해서 v로 가는 도착지가 있는 경우를 매번 구해야 함
        # 근데 노드가 최대 100개니까 이것도 그렇게 오래 걸리지는 않을 거임. 일단 이렇게 해보자...
        def has_path(u, v):
            q = collections.deque([u])
            visited = set([u])

            while q:
                node = q.popleft()
                if node == v:
                    return True
                
                for nei in graph[node]:
                    if nei not in visited:
                        q.append(nei)
                        visited.add(nei)
            
            return False


        graph = {i: [] for i in range(numCourses)}

        for start, end in prerequisites:
            graph[start].append(end)
        
        res = []
        for u, v in queries:
            res.append(has_path(u, v))
        
        return res