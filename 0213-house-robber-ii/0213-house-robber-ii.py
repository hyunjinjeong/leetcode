class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp인데... dp[i+1] = max(dp[i-1]+nums[i], dp[i])
        # 문제는 index 0, -1이 이어져 있다는 전제.
        # 케이스를 두 가지로 나누면 됨. 0~n-2, 1~n-1.
        # 엣지 케이스
        if len(nums) == 1:
            return nums[0]

        return max(self.get_max_money(0, len(nums)-1, nums), self.get_max_money(1, len(nums), nums))
    
    def get_max_money(self, left, right, nums):
        prev, curr = 0, 0
        for i in range(left, right):
            tmp_curr = curr
            
            curr = max(curr, prev + nums[i])
            prev = tmp_curr
        
        return curr