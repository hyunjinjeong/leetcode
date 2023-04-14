class Solution:
    def numDecodings(self, s: str) -> int:
        # 0 < s[n] <= 9 이면 dp[n] += dp[n-1]
        # 그리고 10 <= s[n-2:n] <= 26 이면 dp[n] += dp[n-2]
        # 둘을 각각 따로 계산하는 게 핵심...
        
        if s[0] == "0": # leading zero. 에러 케이스 처리
            return 0
        
        dp = [0] * (len(s)+1)
        # 초기화
        dp[0] = 1
        dp[1] = 1
        
        for i in range(2, len(s)+1):
            if 0 < int(s[i-1]) <= 9:
                dp[i] += dp[i-1]
            if 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]
        
        return dp[-1]
        