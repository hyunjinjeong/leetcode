class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # brute force로 풀면 2^n이고...
        # top down으로 풀면 쉬움

        dp = {}

        def dfs(i, curr_value):
            if i == len(nums):
                dp[(i, curr_value)] = 1 if curr_value == target else 0
            if (i, curr_value) in dp:
                return dp[(i, curr_value)]    

            positive = dfs(i + 1, curr_value + nums[i])
            negative = dfs(i + 1, curr_value - nums[i])
            
            dp[(i, curr_value)] = positive + negative
            return dp[(i, curr_value)]
        
        return dfs(0, 0)
