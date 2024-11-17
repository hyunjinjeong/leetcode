class Solution:
    def numSquares(self, n: int) -> int:
        # perfect square라면.. sqrt(n)까지겠네
        @cache
        def dfs(num_left):
            if num_left == 0:
                return 0
            
            res = float("inf")
            for num in range(1, int(sqrt(num_left)) + 1):
                res = min(res, dfs(num_left - num ** 2) + 1)
            
            return res
        
        return dfs(n)