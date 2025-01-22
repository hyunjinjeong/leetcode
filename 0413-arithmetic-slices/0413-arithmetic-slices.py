class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        N = len(nums)
        res = 0

        prev_count, curr_count = 0, 0
        for i in range(2, N):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                curr_count += prev_count + 1
                res += curr_count
                
            prev_count, curr_count = curr_count, 0
        
        return res