class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        # array가 1..n까지 있는데 inverse pair가 k개 있어야 함
        # n = 1 => [1]밖에 없음. 즉 inverse pair는 0개.
        # n = 2 => [1, 2], [2, 1]. inverse pair는 0개, 1개.
        # n = 3 => [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]
        #           inverse pair는 0개, 1개, 1개, 2개, 2개, 3개
        # 4 3 2 1이면 43 42 41 32 31 21 

        # inverse pair는 0 ~ nC2 개까지 가능. 
        # 딱봐도 DP인데 어떻게 subproblem을 정의하지...

        # x + p = k.... 새로 숫자를 추가할 때 오른쪽에서부터 k - i번째에 넣으면 전체가 k개가 된다.
        # 즉 새로운 숫자를 어느 위치에 넣는지
        # MOD = 10 ** 9 + 7

        # @cache
        # def count(n, k):
        #     if n == 0:
        #         return 1 if k == 0 else 0
        #     if k < 0:
        #         return 0
            
        #     res = 0
        #     for i in range(n):
        #         res = (res + count(n - 1, k - i)) % MOD
            
        #     return res
        
        # return count(n, k)
        
        MOD = 10**9 + 7
        dp = [0] * (k + 1)
        dp[0] = 1

        for N in range(1, n + 1):
            new_dp = [0] * (k + 1)
            total = 0 # sliding window
            for K in range(k + 1):
                if K >= N:
                    total -= dp[K - N]
                total = (total + dp[K]) % MOD
                new_dp[K] = total
            dp = new_dp
        
        return dp[k]