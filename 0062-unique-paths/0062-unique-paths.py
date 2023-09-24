class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # # dp...
        # dp = [[0] * n for _ in range(m)]

        # # 초기화
        # for i in range(m):
        #     dp[i][0] = 1
        # for j in range(n):
        #     dp[0][j] = 1
        
        # for i in range(1, m):
        #     for j in range(1, n):
        #         dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        # return dp[m-1][n-1]

        # 이건 O(n) 공간 버전. DP 배열에서 바로 전 row만 사용한다는 점 이용
        dp = [1] * n
        
        for _ in range(1, m):
            for j in range(1, n):
                # row 단위로 계속 덮어 씌우면서 업데이트
                dp[j] += dp[j-1]
        
        return dp[n-1]