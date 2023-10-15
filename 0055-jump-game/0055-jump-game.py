class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # # dp?
        # N = len(nums)

        # dp = [False] * N
        # dp[N - 1] = True

        # for i in range(N - 2, -1, -1):
        #     max_len = nums[i]

        #     if i + max_len >= N - 1:
        #         dp[i] = True
        #     else:
        #         for length in range(1, max_len + 1):
        #             dp[i] = dp[i + length] or dp[i]
        #             if dp[i]:
        #                 break
        
        # return dp[0]

        # greedy가 됨. 항상 마지막 인덱스까지 볼 필요 없이 중간중간 갱신하면서...
        last_index = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= last_index:
                last_index = i
        
        return last_index == 0