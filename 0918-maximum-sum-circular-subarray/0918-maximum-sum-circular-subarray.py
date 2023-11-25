class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # hint를 보면.. 
        # The maximum result equals to the total sum minus the minimum subarray sum.
        # 직관적으로 이해가 안 된다.
        global_max, global_min = nums[0], nums[0]
        curr_max, curr_min = 0, 0
        total_sum = 0
        
        for num in nums:
            total_sum += num
            
            curr_max = max(curr_max + num, num)
            curr_min = min(curr_min + num, num)
            
            global_max = max(curr_max, global_max)
            global_min = min(curr_min, global_min)
            
        return max(total_sum - global_min, global_max) if global_max > 0 else global_max