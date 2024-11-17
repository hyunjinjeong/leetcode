class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if len(jobDifficulty) < d:
            return -1
        
        # # so how should I assign...
        # # first the jobs should be assigned in order
        # # so we can't use sorting here
        # # d <= 10 and len(jobDifficulty) <= 300.
        # # can I use stack here? I don't think so
        # # so it seems like it's DP or backtracking.
        # # and my intuition is it's most likely DP.
        # @cache
        # def dfs(start, day):
        #     if day == d:
        #         return max(jobDifficulty[start:])

        #     res = float("inf")
            
        #     curr_max = 0
        #     for i in range(start, len(jobDifficulty) - (d - day)):
        #         curr_max = max(curr_max, jobDifficulty[i])
        #         res = min(res, curr_max + dfs(i + 1, day + 1))

        #     return res        

        # return dfs(0, 1)

        # bottom-up dp
        N = len(jobDifficulty)
        if N < d:
            return -1

        daily_min_diff = [float("inf")] * N + [0]

        for days_remaining in range(1, d + 1):
            next_daily_min_diff = [float("inf")] * N + [0]
            for i in range(N - days_remaining + 1):
                daily_max = 0
                for j in range(i + 1, N - days_remaining + 2):
                    daily_max = max(daily_max, jobDifficulty[j - 1])
                    next_daily_min_diff[i] = min(next_daily_min_diff[i], daily_max + daily_min_diff[j])
            daily_min_diff = next_daily_min_diff

        return daily_min_diff[0]