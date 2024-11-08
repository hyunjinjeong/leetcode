class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        # root에서 시작하면 가지가 갈라지는 경우가 계산이 안되는구나
        def dfs(city):
            visited.add(city)

            sub_cost, sub_count = 0, 0
            for nei in graph[city]:
                if nei in visited:
                    continue
                
                sub_result = dfs(nei)
                sub_cost += sub_result[0]
                sub_count += sub_result[1]
            
            count = 1 + sub_count
            cost = max(1, math.ceil(count / seats)) + sub_cost

            return (cost, count)

        N = len(roads)
        graph = {i: [] for i in range(N + 1)}

        for src, dst in roads:
            graph[src].append(dst)
            graph[dst].append(src)

        visited = set()
        visited.add(0)

        res = 0
        for nei in graph[0]:
            res += dfs(nei)[0]

        return res