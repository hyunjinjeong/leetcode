class Solution:
    def rob(self, nums: List[int]) -> int:
        # 0과 -1이 이웃이라는 조건이 추가되었다!
        # 오.. 몰르겠어서 힌트를 보니 결국 0~n-1 이랑 1~n으로 나눠진다는 설명!
        # 그러고 나면 위와 동일한 문제.
        if len(nums) == 1:
            return nums[0]
        
        return max(self.get_rob(nums[1:]), self.get_rob(nums[:-1]))
        
    def get_rob(self, nums):
        dp = [0] * (len(nums)+1)
        dp[1] = nums[0]
        
        for i in range(1, len(nums)):
            dp[i+1] = max(dp[i], dp[i-1]+nums[i])
        
        return dp[-1]