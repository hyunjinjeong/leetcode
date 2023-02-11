class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_sum = [1] * len(nums)
        suffix_sum = [1] * len(nums)
        prefix_sum[0] = nums[0]
        suffix_sum[-1] = nums[-1]
        
        for i in range(1, len(nums)):
            prefix_sum[i] = prefix_sum[i-1] * nums[i]
        
        for i in range(len(nums)-2, -1, -1):
            suffix_sum[i] = suffix_sum[i+1] * nums[i]
        
        answer = [1] * len(nums)
        answer[0] = suffix_sum[1]
        answer[-1] = prefix_sum[-2]
        
        for i in range(1, len(nums)-1):
            answer[i] = prefix_sum[i-1] * suffix_sum[i+1]
        
        return answer