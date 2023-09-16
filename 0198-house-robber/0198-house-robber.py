class Solution:
    def rob(self, nums: List[int]) -> int:
        # # dp. dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        # N = len(nums)
        # # 엣지 케이스
        # if N == 1:
        #     return nums[0]
        # if N == 2:
        #     return max(nums[0], nums[1])

        # dp = [0] * N
        # dp[0] = nums[0]
        # dp[1] = max(nums[0], nums[1])

        # for i in range(2, N):
        #     dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        
        # return dp[N-1]

        # dp 배열에서 마지막 2개만 쓰고 있으니까 변수 두 개로 최적화도 가능
        prev, curr = 0, 0
        for num in nums:
            tmp_prev = prev
            
            prev = curr
            curr = max(curr, tmp_prev + num)
        
        return curr