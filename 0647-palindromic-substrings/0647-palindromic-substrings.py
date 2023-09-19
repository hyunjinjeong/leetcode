class Solution:
    def countSubstrings(self, s: str) -> int:
        N = len(s)
        dp = [[False] * N for _ in range(N)]

        ans = 0
        for start in range(N-1, -1, -1):
            for end in range(start, N):
                if start == end:
                    dp[start][end] = True
                elif start + 1 == end:
                    dp[start][end] = s[start] == s[end]
                else:
                    dp[start][end] = s[start] == s[end] and dp[start+1][end-1]
                
                if dp[start][end]:
                    ans += 1
        
        return ans