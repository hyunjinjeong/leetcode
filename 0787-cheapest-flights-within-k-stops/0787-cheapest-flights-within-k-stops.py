class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # 다익스트라 쓰기..?
        # bfs 돌려서 k번 체크하는 방법도 있을 듯.
        
        # 그래프 만들기
        graph = collections.defaultdict(list)
        for flight in flights:
            _from, to, price = flight
            graph[_from].append((to, price))
        
        # bfs로 체크
        q = collections.deque([(src, 0)])
        
        cheapest_prices = [float("inf")] * (n + 1)
        stops = 0
        ans = float("inf")
        while q and stops <= k:
            for _ in range(len(q)):
                curr_city, curr_price = q.popleft()
                if curr_city not in graph:
                    continue
                
                for adj, price in graph[curr_city]:
                    # 쌩 bfs는 TLE 떠서 최적화..
                    if curr_price + price >= cheapest_prices[adj]:
                        continue
                    
                    cheapest_prices[adj] = curr_price + price
                    q.append((adj, curr_price + price))
                    
            stops += 1
        
        return cheapest_prices[dst] if cheapest_prices[dst] != float("inf") else -1