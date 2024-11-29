class Solution:
    def numTrees(self, n: int) -> int:
        
        @cache
        def dfs(start, end):
            res = 0
            for root in range(start, end + 1):
                left = dfs(start, root - 1) or 1
                right = dfs(root + 1, end) or 1
                res += left * right

            return res

        
        return dfs(1, n)