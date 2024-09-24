class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        # 매번 1 ~ maxPts 사이의 점수를 얻는거고... 점수가 k를 넘으면 종료함. 이 때 포인트가 n보다 작아야 함
        # 그럼 확률을 저장해서.. dp를 돌 수 있으려나?
        # 뭐에 대한 확률인지를 정의해야 함...
        # 길이는 maxPts로..? 그리고 k번 하면서 계속 업데이트하면 되지 않을까
        # k번이 아니구나... 이전에 k를 넘기면 더 플레이할 필요가 없으니까
        
        # @cache
        # def dfs(pts):
        #     if pts >= k:
        #         return 1.0 if pts <= n else 0.0
            
        #     res = 0
        #     for i in range(1, maxPts + 1):
        #         res += dfs(pts + i)
            
        #     return res / maxPts
        
        # return dfs(0)

        # 위에꺼 TLE 뜸... 아래는 optimal인데 이해가 안 된다. 그냥 넘어가자.
        if k == 0 or n >= k + maxPts:
            return 1.0
        
        dp = [1.0] + [0.0] * n
        w_sum = 1.0

        for i in range(1, n + 1):
            dp[i] = w_sum / maxPts
            if i < k:
                w_sum += dp[i]
            if i - maxPts >= 0:
                w_sum -= dp[i - maxPts]
        
        return sum(dp[k:])