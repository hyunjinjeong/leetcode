class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp인데... dp[i+1] = max(dp[i-1]+nums[i], dp[i])
        # 문제는 index 0, -1이 이어져 있다는 전제.
        # 케이스를 두 가지로 나누면 됨. 0~n-2, 1~n-1.
        # 엣지 케이스
        if len(nums) == 1:
            return nums[0]
        
        # 1. 0~n-2
        prev, curr = 0, 0
        for i in range(len(nums)-1):
            tmp_curr = curr
            
            curr = max(curr, prev + nums[i])
            prev = tmp_curr
        ans = curr

        # 2. 1~n-1
        prev, curr = 0, 0
        for i in range(1, len(nums)):
            tmp_curr = curr
            
            curr = max(curr, prev + nums[i])
            prev = tmp_curr
        ans = max(curr, ans)

        return ans