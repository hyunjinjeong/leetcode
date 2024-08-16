class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0] * (days[-1] + 1)
        days_set = set(days)

        # DP인가?
        # 1일짜리, 7일짜리, 30일짜리 할 수 있고
        # 슉슉 넘어가면 될거 같은데
        # dp[i]가 있을 때.. dp[i] = min(dp[i-30] + costs[2], dp[i-7] + costs[1], dp[i-1] + costs[0]) 인가?
        for day in range(1, len(dp)):
            if day not in days_set:
                dp[day] = dp[day - 1]
            else:
                # 오 이렇게 할 수도 있구나
                dp[day] = min(dp[day - 1] + costs[0], dp[max(day - 7, 0)] + costs[1], dp[max(day - 30, 0)] + costs[2])
                # if day < 7:
                #     dp[day] = min(dp[day - 1] + costs[0], costs[1], costs[2])
                # elif day < 30:
                #     dp[day] = min(dp[day - 1] + costs[0], dp[day - 7] + costs[1], costs[2])
                # else:
                #     dp[day] = min(dp[day - 1] + costs[0], dp[day - 7] + costs[1], dp[day - 30] + costs[2])

        return dp[-1]