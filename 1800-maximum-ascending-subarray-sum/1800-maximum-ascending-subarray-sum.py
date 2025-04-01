class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum, curr_sum = 0, 0
        prev = nums[0]
        
        for num in nums:
            if num > prev:
                curr_sum += num
            else:
                curr_sum = num
            max_sum = max(curr_sum, max_sum)
            prev = num
        
        return max_sum