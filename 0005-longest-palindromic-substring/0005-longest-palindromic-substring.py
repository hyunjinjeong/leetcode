class Solution:
    def longestPalindrome(self, s: str) -> str:
        # dp...
        # 베이스는 1개일 때는 항상 true, 2개일 때는 같으면 true
        # 그 뒤로는 lo+1, hi-1이 dp인지 확인
        N = len(s)
        dp = [[False] * N for _ in range(N)]
        
        left, right = 0, 1
        for start in range(N-1, -1, -1):
            for end in range(start, N):
                if start == end: # 1개
                    dp[start][end] = True
                elif end == start + 1: # 2개
                    dp[start][end] = s[start] == s[end]
                else:
                    dp[start][end] = s[start] == s[end] and dp[start+1][end-1]

                if end + 1 - start > right - left and dp[start][end]:
                    left, right = start, end + 1
        
        return s[left:right]