class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        # root에서 시작하면 가지가 갈라지는 경우가 계산이 안되는구나
        def dfs(city, prev):
            count = 0
            for nei in graph[city]:
                if nei == prev:
                    continue
                sub_count = dfs(nei, city)
                self.res += math.ceil(sub_count / seats)
                count += sub_count
            
            return count + 1

        N = len(roads)
        graph = {i: [] for i in range(N + 1)}

        for src, dst in roads:
            graph[src].append(dst)
            graph[dst].append(src)

        self.res = 0
        dfs(0, -1)

        return self.res