class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        N = len(nums)
        prefix_sum = [0] * (N + 1)
        for i in range(1, N + 1):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]
        
        @cache
        def dfs(start, part):
            if part == k:
                return prefix_sum[N] - prefix_sum[start]

            res = float("inf")
            for i in range(start, N - (k - part)):
                curr = prefix_sum[i + 1] - prefix_sum[start]
                rest = dfs(i + 1, part + 1)

                res = min(res, max(curr, rest))
        
            return res

        return dfs(0, 1)