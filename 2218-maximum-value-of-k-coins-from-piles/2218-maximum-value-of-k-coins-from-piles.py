class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        # piles[i]가 1, 2, 3 이렇게 있을때 top이 1. bottom이 3. k번 골랐을 때 최적을 구하기.
        # dp를 적용할 수는 있을 듯? k번을 뽑았을 때 최적은 k - 1번을 뽑았을 때의 최적에 현재의 max를 더하면 됨
        # !! 한번에 1개씩 뽑는게 아니라 최대 k개씩 뽑으면서 끝까지 가면 된다.

        # @cache
        # def dfs(pile, steps):
        #     if steps == 0 or pile == len(piles):
        #         return 0

        #     res = 0
        #     for curr_steps in range(min(steps, len(piles[pile])) + 1):
        #         curr_sum = prefix_sums[pile][curr_steps]
        #         res = max(curr_sum + dfs(pile + 1, steps - curr_steps), res)
            
        #     return res
        
        # bottom up으로도 가봅시다

        N = len(piles)
        dp = [0] * (k + 1)

        for i in range(N):
            new_dp = [0] * (k + 1)
            for coins in range(k + 1):
                curr_sum = 0
                for curr_coins in range(min(coins, len(piles[i])) + 1):
                    prev_sum = dp[coins - curr_coins] if i > 0 else 0
                    curr_sum += piles[i][curr_coins - 1] if curr_coins > 0 else 0
                    new_dp[coins] = max(prev_sum + curr_sum, new_dp[coins])
            dp = new_dp

        return dp[k]