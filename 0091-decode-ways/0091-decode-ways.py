class Solution:
    def numDecodings(self, s: str) -> int:
        # 숫자가 10~26 사이면 2가지 경우의 수가 존재하는 것
        # 아 근데 10, 20은 안됨. 하나 뿐.
        # 0 < s[n] <= 9 이면 dp[n] += dp[n-1]
        # 그리고 10 <= s[n-2:n] <= 26 이면 dp[n] += dp[n-2]
        # 둘을 각각 따로 계산하는 게 핵심...
        N = len(s)

        dp = [0] * (N+1)
        # 초기화
        dp[0] = 1
        dp[1] = 1 if s[0] != "0" else 0
        
        for i in range(2, N+1):
            if 0 < int(s[i-1:i]) <= 9: # one step
                dp[i] += dp[i-1]
            if 10 <= int(s[i-2:i]) <= 26: # two step
                dp[i] += dp[i-2]
        
        return dp[N]
        