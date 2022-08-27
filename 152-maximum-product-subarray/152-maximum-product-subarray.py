class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # 핵심은 곱하기는 음수가 될 수도 있으니까 curr_min도 같이 관리하는 것!
        curr_max, curr_min, ans = nums[0], nums[0], nums[0]
        
        for i in range(1, len(nums)):
            num = nums[i]
            
            # 아 그냥 하면 curr_max가 업뎃되는구나;
            tmp_curr_max = max(curr_max * num, curr_min * num, num)
            tmp_curr_min = min(curr_min * num, curr_max * num, num)
            
            curr_max, curr_min = tmp_curr_max, tmp_curr_min
            ans = max(curr_max, ans)
        
        return ans