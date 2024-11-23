class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        # cost가 낮은 순서대로 paid painter를 쓰고 높은건 free painter를 쓰면 좋음
        # 그런데 free는 paid가 이미 사용 중인 경우에만 쓸 수 있으니까...
        # 그럼 time 기준 sum(paid_time) <= ceil(time / 2) 동안 paid를 써야 함
        N = len(cost)
        PAID_MAX_TIME = math.ceil(sum(time) / 2)

        total_paid_time = 0

        
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
