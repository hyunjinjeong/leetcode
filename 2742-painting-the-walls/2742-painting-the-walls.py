class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        # 걍 0-1 knapsack이구나
        N = len(cost)

        @cache
        def dfs(i, count):
            if count >= N:
                return 0
            if i == N:
                return float("inf")
            
            use = cost[i] + dfs(i + 1, count + time[i] + 1)
            not_use = dfs(i + 1, count)

            return min(use, not_use)
        
        return dfs(0, 0)
