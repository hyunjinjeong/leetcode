class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 전형적인 topological sort...
        graph = {i: set() for i in range(numCourses)}
        in_degree = {i: 0 for i in range(numCourses)}

        # 그래프 초기화
        for _to, _from in prerequisites:
            graph[_from].add(_to)
            in_degree[_to] += 1
        
        q = collections.deque()
        # queue 초기화
        for course in range(numCourses):
            if in_degree[course] == 0:
                q.append(course)
        
        ans = []
        while q:
            course = q.popleft()
            ans.append(course)

            for next_course in graph[course]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    q.append(next_course)
        
        return ans if len(ans) == numCourses else []