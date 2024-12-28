class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        # # dp?

        # @cache
        # def dfs(i):
        #     if i == len(s):
        #         return 0

        #     # 걸리는게 있으면 dfs(i + len(word)) 하고
        #     # 없으면..? dfs(i + 1)로 가야 함
        #     pick = float("inf")
        #     for word in dictionary:
        #         if i + len(word) <= len(s) and s[i:i + len(word)] == word:
        #             pick = min(dfs(i + len(word)), pick)
            
        #     not_pick = 1 + dfs(i + 1)
        #     return min(pick, not_pick)
        
        # return dfs(0)

        # bottom up

        word_set = set(dictionary)

        N = len(s)
        dp = [0] * (N + 1)

        for i in range(N - 1, -1, -1):
            dp[i] = dp[i + 1] + 1
            for j in range(i, N):
                word = s[i:j + 1]
                if word in word_set:
                    dp[i] = min(dp[j + 1], dp[i])
            
        return dp[0]