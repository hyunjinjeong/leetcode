class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        global_max = nums[0]
        curr_max = 0
        
        for num in nums:
            curr_max = max(curr_max + num, num)
            global_max = max(curr_max, global_max)
        
        return global_max