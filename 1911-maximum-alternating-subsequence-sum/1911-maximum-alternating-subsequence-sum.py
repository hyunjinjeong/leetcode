class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        # 일단 갯수는 무조건 홀수여야 함. 짝수번은 -가 되니까. 1, 3, 5, ...
        # 짝수 인덱스는 최대한 작게, 홀수 인덱스는 최대한 크게 해야 함.
        # 이거 그냥 0-1 knapsack 같은데... 

        @cache
        def dfs(i, is_odd):
            if i == len(nums):
                return 0

            not_pick = dfs(i + 1, is_odd)

            num = nums[i] if is_odd else -nums[i]
            pick = num + dfs(i + 1, not is_odd)

            return max(pick, not_pick)
        
        return dfs(0, True)