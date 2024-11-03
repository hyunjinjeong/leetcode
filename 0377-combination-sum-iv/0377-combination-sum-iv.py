class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # backtracking?
        
        @cache
        def dfs(current):
            if current > target:
                return 0
            if current == target:
                return 1
            
            res = 0
            for i in range(len(nums)):
                res += dfs(current + nums[i])
            
            return res
        
        return dfs(0)