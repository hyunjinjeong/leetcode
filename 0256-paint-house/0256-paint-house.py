class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        # 모든 경우의 수를 다 찾으면 되지 않을까?
        # RED, BLUE, GREEN = 0, 1, 2

        # @cache
        # def dfs(i, curr, prev_color):
        #     if i == len(costs):
        #         return curr

        #     if prev_color == RED:
        #         blue = dfs(i + 1, curr + costs[i][BLUE], BLUE)
        #         green = dfs(i + 1, curr + costs[i][GREEN], GREEN)
        #         return min(blue, green)
        #     elif prev_color == BLUE:
        #         red = dfs(i + 1, curr + costs[i][RED], RED)
        #         green = dfs(i + 1, curr + costs[i][GREEN], GREEN)
        #         return min(red, green)
        #     elif prev_color == GREEN:
        #         red = dfs(i + 1, curr + costs[i][RED], RED)
        #         blue = dfs(i + 1, curr + costs[i][BLUE], BLUE)
        #         return min(red, blue)
        #     else:
        #         red = dfs(i + 1, curr + costs[i][RED], RED)
        #         blue = dfs(i + 1, curr + costs[i][BLUE], BLUE)
        #         green = dfs(i + 1, curr + costs[i][GREEN], GREEN)
        #         return min(red, blue, green)
        
        # return dfs(0, 0, None)

        # 요건 bottom up DP로 다시 풀 수 있겠구만
        RED, BLUE, GREEN = 0, 1, 2
        dp = [[0] * 3 for _ in range(len(costs))]
        dp[0] = costs[0]

        for i in range(1, len(costs)):
            dp[i][RED] = costs[i][RED] + min(dp[i-1][BLUE], dp[i-1][GREEN])
            dp[i][BLUE] = costs[i][BLUE] + min(dp[i-1][RED], dp[i-1][GREEN])
            dp[i][GREEN] = costs[i][GREEN] + min(dp[i-1][RED], dp[i-1][BLUE])

        return min(dp[-1])