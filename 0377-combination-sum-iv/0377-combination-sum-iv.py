class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # # backtracking?
        
        # @cache
        # def dfs(current):
        #     if current > target:
        #         return 0
        #     if current == target:
        #         return 1
            
        #     res = 0
        #     for i in range(len(nums)):
        #         res += dfs(current + nums[i])
            
        #     return res
        
        # return dfs(0)

        # bottom up dp
        dp = [0] * (target + 1)
        dp[0] = 1

        for curr in range(1, target + 1):
            for num in nums:
                if curr >= num:
                    dp[curr] += dp[curr - num]
        
        return dp[target]