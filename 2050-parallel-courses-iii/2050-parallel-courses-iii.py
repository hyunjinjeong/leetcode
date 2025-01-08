class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        # topological sort -> bfs?
        # 특정 수업 관점에서, 자신을 향하는 이전 수업들 중 max 값에 자신의 값을 더한 값이 해당 수업을 듣는데 필요한 값
        # 그러면 in_degree가 0인 노드만 추가하고..
        # 노드별 최댓값..?을 저장하는 자료구조가 필요할 듯. 걍 배열로 해도 되겠다
        max_time_courses = time[:]
        graph = {i: [] for i in range(n)}
        in_degrees = [0] * n
        
        for start, end in relations:
            graph[start - 1].append(end - 1)
            in_degrees[end - 1] += 1
        
        q = collections.deque()
        for course in range(n):
            if in_degrees[course] == 0:
                q.append(course)

        while q:
            course = q.popleft()
            
            for neighbor in graph[course]:
                max_time_courses[neighbor] = max(max_time_courses[course] + time[neighbor], max_time_courses[neighbor])
                in_degrees[neighbor] -= 1
                if in_degrees[neighbor] == 0:
                    q.append(neighbor)
        
        return max(max_time_courses)