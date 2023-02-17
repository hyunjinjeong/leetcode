class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(start, current_array, current_sum):
            if current_sum > target:
                return
            
            if current_sum == target:
                ans.append(current_array)
                return 
            
            for i in range(start, len(candidates)):
                val = candidates[i]
                dfs(i, current_array + [val], current_sum + val)
        
        ans = []
        dfs(0, [], 0)
        
        return ans