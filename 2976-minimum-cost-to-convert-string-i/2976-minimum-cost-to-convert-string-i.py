class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        # 그래프의 냄새가 난다
        def get_min_costs(src):
            heap = [(0, src)]
            min_costs = collections.defaultdict(lambda: float("inf"))

            while heap:
                curr_cost, node = heapq.heappop(heap)
                if node in min_costs:
                    continue
                min_costs[node] = curr_cost

                for adj, adj_cost in edges[node]:
                    heapq.heappush(heap, (curr_cost + adj_cost, adj))

            return min_costs
        
        lower_alphabets = "abcdefghijklmnopqrstuvwxyz"

        edges = {c: [] for c in lower_alphabets}
        for src, dst, curr_cost in zip(original, changed, cost):
            edges[src].append((dst, curr_cost))
        
        min_costs = {c: get_min_costs(c) for c in lower_alphabets}
        
        min_cost = 0
        for i in range(len(source)):
            if source[i] == target[i]:
                continue
            
            curr_min_cost = min_costs[source[i]][target[i]]
            if curr_min_cost == float("inf"):
                return -1
            min_cost += curr_min_cost
        
        return min_cost
