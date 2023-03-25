class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # topological sort?
        graph = {i:set() for i in range(numCourses)}
        in_degrees = {i:0 for i in range(numCourses)}
        
        # 그래프 만들기
        for child, parent in prerequisites:
            graph[parent].add(child)
            in_degrees[child] += 1
        
        queue = collections.deque()
        
        # in_degree가 0이면 다 추가
        for key in in_degrees:
            if in_degrees[key] == 0:
                queue.append(key)
        
        # 본격 위상 정렬
        ans = []
        while queue:
            vertex = queue.popleft()
            ans.append(vertex)
            for child in graph[vertex]:
                in_degrees[child] -= 1
                if in_degrees[child] == 0:
                    queue.append(child)
        
        return ans if len(ans) == numCourses else []
