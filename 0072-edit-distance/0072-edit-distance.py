class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # 3가지 연산을 다 해보는 방법밖에 없을 것 같은데?
        # 우선 dfs로
        # def dfs(i, j, cache):
        #     if i == len(word1) and j == len(word2):
        #         return 0
        #     if i == len(word1):
        #         return len(word2) - j
        #     if j == len(word2):
        #         return len(word1) - i
            
        #     if (i, j) in cache:
        #         return cache[(i, j)]
            
        #     if word1[i] == word2[j]:
        #         return dfs(i + 1, j + 1, cache)
            
        #     insert = 1 + dfs(i, j + 1, cache)
        #     delete = 1 + dfs(i + 1, j, cache)
        #     replace = 1 + dfs(i + 1, j + 1, cache)

        #     cache[(i, j)] = min(insert, delete, replace)
        #     return cache[(i, j)]
        
        # return dfs(0, 0, {})
        
        # bottom-up으로
        M, N = len(word1), len(word2)
        dp = [[0] * (N + 1) for _ in range(M + 1)]

        for i in range(M + 1):
            dp[i][0] = i
        for j in range(N + 1):
            dp[0][j] = j
        
        for i in range(1, M + 1):
            for j in range(1, N + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])
        
        return dp[M][N]