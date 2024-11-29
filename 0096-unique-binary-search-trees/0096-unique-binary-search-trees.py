class Solution:
    def numTrees(self, n: int) -> int:
        
        # @cache
        # def dfs(start, end):
        #     res = 0
        #     for root in range(start, end + 1):
        #         left = dfs(start, root - 1) or 1
        #         right = dfs(root + 1, end) or 1
        #         res += left * right

        #     return res

        
        # return dfs(1, n)

        dp = [0] * (n + 1)
        dp[0] = 1

        for node in range(1, n + 1):
            for root in range(1, node + 1):
                left = root - 1
                right = node - root
                dp[node] += dp[left] * dp[right]

        return dp[n]