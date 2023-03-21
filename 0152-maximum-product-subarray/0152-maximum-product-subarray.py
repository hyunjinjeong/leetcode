class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_max, curr_min, ans = nums[0], nums[0], nums[0]
        
        for i in range(1, len(nums)):
            num = nums[i]
            
            # max와 min을 둘 다 관리하는 것이 핵심!
            tmp_curr_max = max(curr_max * num, curr_min * num, num)
            tmp_curr_min = min(curr_min * num, curr_max * num, num)
            
            curr_max, curr_min = tmp_curr_max, tmp_curr_min
            ans = max(curr_max, ans)
        
        return ans