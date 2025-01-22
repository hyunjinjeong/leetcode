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
                prev_count = dp[j][diff] if diff in dp[j] else 0
                dp[i][diff] = dp[i].get(diff, 0) + prev_count + 1
                res += prev_count # 이래야 3개짜리부터 res에 더해짐

        return res