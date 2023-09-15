class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # BFS?
        # 단순 BFS는 memory limit이 뜨넹
        graph = collections.defaultdict(list)
        for u, v, price in flights:
            graph[u].append((price, v))
        
        q = collections.deque([(0, src, 0)])
        price_map = {}

        while q:
            price, u, stop = q.popleft()
            if price < price_map.get(u, float("inf")):
                price_map[u] = price
                for next_price, v in graph[u]:
                    if stop <= k:
                        q.append((price + next_price, v, stop + 1))
        
        return price_map.get(dst, -1)