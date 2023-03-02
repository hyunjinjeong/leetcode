class Solution:
    def canPartition(self, nums: List[int]) -> bool:
#         # top-down DP
#         @cache
#         def subset_sum(s, i):
#             if s == 0:
#                 return True
#             if i >= len(nums) or s < 0:
#                 return False
#             return subset_sum(s-nums[i], i+1) or subset_sum(s, i+1)
        
#         total_sum = sum(nums)
#         if total_sum % 2 == 1:
#             return False
#         return subset_sum(total_sum // 2, 0)
        
        # bottom-up DP
        total_sum = sum(nums)
        if total_sum % 2 == 1:
            return False
        
        target_sum = total_sum // 2
        dp = [True] + [False] * target_sum
        for num in nums:
            for curr in range(target_sum, num-1, -1):
                dp[curr] = dp[curr] or dp[curr-num]
        return dp[-1]