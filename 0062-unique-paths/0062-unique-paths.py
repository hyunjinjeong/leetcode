class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp[i][j]를 grid[i][j]에서의 unique path 갯수라고 하면..
        # 기본적으로 dp[i][j] = dp[i-1][j] + dp[i][j-1] 가 될건데
        # 코너 케이스는 i나 j가 0인 경우? 다 1로 처리해주기.
        
        # 애초에 처음부터 1로 초기화하면 되는구나..
#         dp = [[1] * n for _ in range(m)]
        
#         for i in range(1, m):
#             for j in range(1, n):
#                 dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
#         return dp[-1][-1]
    
        # 이건 O(n) 공간 버전. DP 배열에서 바로 전 row만 사용한다는 점 이용
        dp = [1] * n
        
        for _ in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j-1]
        
        return dp[-1]