class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp[n]을 n일 때의 최댓값이라고 하면.. dp[n] = max(dp[n-1], dp[n-2]+nums[n]) 이렇게 되지 않을까
        # 아.. 2, 1, 1, 2 이런 경우는 이게 안되네.
        # 그럼 dp[n-1]이랑 dp[n-2] + nums[n], dp[n-3] + nums[n]... 이렇게 다 비교해야 할 듯?
        dp = [0] * len(nums)
        
        # 엣지 케이스
        dp[0] = nums[0]
        if len(nums) > 1:
            dp[1] = nums[1]
        
        for i in range(2, len(nums)):
            for j in range(i-2, -1, -1):
                # 중간에 덮어 씌워질 수 있어서 자기 자신과도 비교해야     
                dp[i] = max(dp[i], dp[i-1], dp[j]+nums[i])
        
        return max(dp)