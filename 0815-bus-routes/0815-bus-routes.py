class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        # bus stop을 최소화하는게 아니라... bus를 최소화해야 함
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