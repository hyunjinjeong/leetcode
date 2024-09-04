class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        # 모든 경우의 수를 다 찾으면 되지 않을까?
        RED, BLUE, GREEN = 0, 1, 2

        @cache
        def dfs(i, curr, prev_color):
            if i == len(costs):
                return curr

            if prev_color == RED:
                blue = dfs(i + 1, curr + costs[i][BLUE], BLUE)
                green = dfs(i + 1, curr + costs[i][GREEN], GREEN)
                return min(blue, green)
            elif prev_color == BLUE:
                red = dfs(i + 1, curr + costs[i][RED], RED)
                green = dfs(i + 1, curr + costs[i][GREEN], GREEN)
                return min(red, green)
            elif prev_color == GREEN:
                red = dfs(i + 1, curr + costs[i][RED], RED)
                blue = dfs(i + 1, curr + costs[i][BLUE], BLUE)
                return min(red, blue)
            else:
                red = dfs(i + 1, curr + costs[i][RED], RED)
                blue = dfs(i + 1, curr + costs[i][BLUE], BLUE)
                green = dfs(i + 1, curr + costs[i][GREEN], GREEN)
                return min(red, blue, green)
        
        return dfs(0, 0, None)