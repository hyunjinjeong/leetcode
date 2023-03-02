class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        @cache
        def subset_sum(s, i):
            if s == 0:
                return True
            if i >= len(nums) or s < 0:
                return False
            return subset_sum(s-nums[i], i+1) or subset_sum(s, i+1)
        
        total_sum = sum(nums)
        if total_sum % 2 == 1:
            return False
        return subset_sum(total_sum // 2, 0)