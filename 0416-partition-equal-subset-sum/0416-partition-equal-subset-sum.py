class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # sorting...은 안 되는게 1 6 11 6 같은 경우가 있음
        # dp...
        # 핵심은 total_sum // 2가 되는 경우가 있는지 확인하는 것
        total_sum = sum(nums)
        if total_sum % 2 == 1:
            return False
        
        half_sum = total_sum // 2
        dp = [True] + [False] * half_sum
        for num in nums:
            for curr in range(half_sum, num-1, -1):
                dp[curr] = dp[curr-num] or dp[curr]

        return dp[half_sum]