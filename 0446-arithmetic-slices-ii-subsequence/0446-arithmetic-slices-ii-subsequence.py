class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        # 길이 3 이상, 모든 연속된 숫자들의 차이가 같아야 함. 같은 조합이 여러번 나와도 상관 없고...

        N = len(nums)

        # 이렇게 하면 로직은 맞는데 TLE 뜸. 개선이 필요하다.
        # @cache
        # def dfs(last, diff):
        #     res = 0
        #     for i in range(last + 1, N):
        #         if nums[i] - nums[last] == diff:
        #             res += 1 + dfs(i, diff)
        #     return res
                
        # res = 0
        # for i in range(N - 2):
        #     for j in range(i + 1, N - 1):
        #         res += dfs(j, nums[j] - nums[i])
        # return res

        # ㅇㅎ.. LIS랑 비슷하게 푸는 거였음
        res = 0
        dp = [{} for _ in range(N)]

        for i in range(N):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] = dp[i].get(diff, 0) + 1
                if diff in dp[j]:
                    dp[i][diff] += dp[j][diff]
                    res += dp[j][diff]

        return res