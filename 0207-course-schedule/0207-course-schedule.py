class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 그래프에 사이클이 없으면 된다. => 위상 정렬 활용. BFS가 더 편함.
        
        graph = {i: set() for i in range(numCourses)}
        in_degrees = {i:0 for i in range(numCourses)}
        
        # 그래프 만들기
        for child, parent in prerequisites:
            graph[parent].add(child)
            in_degrees[child] += 1
        
        queue = deque() # 파이썬은 Queue가 없으니..
        
        # in_degree가 0이면 다 추가
        for key in in_degrees:
            if in_degrees[key] == 0:
                queue.append(key)
        
        # 본격 위상 정렬
        visited = 0
        while queue:
            vertex = queue.popleft()
            visited += 1
            for child in graph[vertex]:
                in_degrees[child] -= 1
                if in_degrees[child] == 0:
                    queue.append(child)
        
        return visited == numCourses
                