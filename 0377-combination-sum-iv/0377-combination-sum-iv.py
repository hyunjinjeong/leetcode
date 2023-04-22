class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # dp였구나..
        # dp[n]: 값이 n일 때의 조합 갯수
        # dp[i] += dp[i-num]
        dp = [0] * (target+1)

        for i in range(1, target+1):
            for num in nums:
                if i < num:
                    continue
                elif i == num: # 엣지 케이스
                    dp[i] += 1
                elif i >= num:
                    dp[i] += dp[i-num]
            
        return dp[-1]