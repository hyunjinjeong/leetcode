class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if len(jobDifficulty) < d:
            return -1
        
        # so how should I assign...
        # first the jobs should be assigned in order
        # so we can't use sorting here
        # d <= 10 and len(jobDifficulty) <= 300.
        # can I use stack here? I don't think so
        # so it seems like it's DP or backtracking.
        # and my intuition is it's most likely DP.
        @cache
        def dfs(start, day):
            if day == d:
                return max(jobDifficulty[start:])

            res = float("inf")
            
            curr_max = 0
            for i in range(start, len(jobDifficulty) - (d - day)):
                curr_max = max(curr_max, jobDifficulty[i])
                res = min(res, curr_max + dfs(i + 1, day + 1))

            return res        

        return dfs(0, 1)