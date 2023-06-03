class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        # 가중치가 없는 그래프.
        # 단방향..? 근데 loop는 있음.
        # 그럼 그래프를 만든 뒤에 BFS 돌리면 안되려나
        # 아 근데 bus stop을 최소화하는게 아니라... bus를 최소화해야 함
        # 
        # 일단 그래프를 만들어보자
        if source == target:
            return 0
        
        stop_to_bus = collections.defaultdict(list)
        for bus, stops in enumerate(routes):
            for stop in stops:
                stop_to_bus[stop].append(bus)
                
        q = collections.deque([(source, 0)])
        visited = set()

        while q:
            stop, count = q.popleft()
            if stop == target:
                return count
            
            for bus in stop_to_bus[stop]:
                if bus in visited:
                    continue

                visited.add(bus)
                for next_stop in routes[bus]:
                    q.append((next_stop, count+1))
        
        return -1