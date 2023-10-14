class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # cache = {}

        # def dfs(i, j):
        #     if i == len(s) and j == len(p):
        #         return True
        #     if j == len(p):
        #         return False
            
        #     if (i, j) in cache:
        #         return cache[(i, j)]
            
        #     match = i < len(s) and (s[i] == p[j] or p[j] == ".")

        #     # * 앞의 캐릭터를 사용하는지 안하는지.
        #     if j + 1 < len(p) and p[j + 1] == "*":
        #         ans = dfs(i, j + 2) or match and dfs(i + 1, j)
        #     else:
        #         ans = dfs(i + 1, j + 1) if match else False
            
        #     cache[(i, j)] = ans
        #     return ans
        
        # return dfs(0, 0)

        # bottom up으로

        M, N = len(s), len(p)
        dp = [[False] * (N + 1) for _ in range(M + 1)]

        # Base case: an empty pattern matches an empty string.
        dp[M][N] = True

        # Filling the table from right to left, bottom to top.
        for i in range(M, -1, -1):
            for j in range(N - 1, -1, -1): # N인 경우는 어차피 False니까...
                match = i < M and (s[i] == p[j] or p[j] == '.')

                if j + 1 < N and p[j + 1] == '*':
                    dp[i][j] = dp[i][j + 2] or (match and dp[i + 1][j])
                else:
                    dp[i][j] = match and dp[i + 1][j + 1]

        return dp[0][0]