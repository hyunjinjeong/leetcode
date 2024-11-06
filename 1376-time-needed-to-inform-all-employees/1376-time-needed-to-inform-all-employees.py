class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # BFS나 DFS 돌려서 마지막 employee인 경우에 값을 계속 갱신하면 될 듯?
        graph = {i:[] for i in range(n)}

        # i번째의 매니저가 manager[i]니까
        # manager[i]의 graph에 i를 추가해줘야 함
        for i in range(n):
            if manager[i] == -1:
                continue
            graph[manager[i]].append(i)

        res = 0
        q = collections.deque([(headID, 0)])

        while q:
            employee, time = q.popleft()
            if not graph[employee]:
                res = max(res, time)
                continue
            
            for next_employee in graph[employee]:
                q.append((next_employee, time + informTime[employee]))
        
        return res