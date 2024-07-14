class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # 흠 A-B difference를 처음부터 썼으면 greedy로 풀 수도 있었네
        costs.sort(key=lambda cost: cost[0] - cost[1])

        ans = 0
        n = len(costs) // 2
        for i in range(n):
            ans += costs[i][0] + costs[i + n][1]
        
        return ans