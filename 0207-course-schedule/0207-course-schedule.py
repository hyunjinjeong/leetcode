class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 간단한 위상 정렬...
        # 초기화
        graph = {i: set() for i in range(numCourses)}
        in_degree = {i:0 for i in range(numCourses)}

        # graph, in_degree 값 할당
        for _to, _from in prerequisites:
            graph[_from].add(_to)
            in_degree[_to] += 1
        
        # Queue 초기화
        q = collections.deque()
        for key in in_degree:
            if in_degree[key] == 0:
                q.append(key)
        
        num_visited = 0
        while q:
            course = q.popleft()
            num_visited += 1
            for next_course in graph[course]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    q.append(next_course)
        
        return num_visited == numCourses