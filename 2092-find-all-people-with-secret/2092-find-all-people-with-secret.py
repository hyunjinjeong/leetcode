class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        # meetings를 시간순으로 정렬하는게 자연스러워 보임
        # 그리고 매 시간마다 둘 중 하나라도 secret을 알면 다른 한명도 추가해야 하고
        # 같은 시간에 여러 미팅이 있으면? 동일한 시간의 전체를 돌고 그 사람들 중 하나라도 secret이 있으면 전체가 secret을 가진다.
        # -> 가 아니고 미팅이 있어야 함.
        # 그러면 그래프 문제 아니면... connected components 문제 같은데
        # 시간대별로 묶으면 되는구나
        
        meetings.sort(key=lambda meeting: meeting[2])

        meetings_by_time = collections.defaultdict(list)
        for x, y, time in meetings:
            meetings_by_time[time].append((x, y))
        
        parent = [i for i in range(n)]
        size = [1] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(u, v):
            pu, pv = find(u), find(v)
            if pu == pv:
                return

            if size[pu] > size[pv]:
                parent[pv] = pu
                size[pu] += size[pv]
            else:
                parent[pu] = pv
                size[pv] += size[pu]
        
        union(0, firstPerson)
        for time in meetings_by_time:
            for x, y in meetings_by_time[time]:
                union(x, y)
            
            for x, y in meetings_by_time[time]:
                if find(x) != find(0): # 같은 시간대 사람 중 비밀을 알고 있는 사람이 있었으면 0이랑 연결되어 있어야 함
                    parent[x], size[x] = x, 1
                    parent[y], size[y] = y, 1
        
        return [i for i in range(n) if find(i) == find(0)]