class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(index, current):
            if index >= len(candidates):
                return
            
            current_sum = sum(current)
            if current_sum > target:
                return
            
            if current_sum == target:
                ans.append(current)
                return 
            
            for i in range(index, len(candidates)):
                dfs(i, current + [candidates[i]])
        
        ans = []
        dfs(0, [])
        
        return ans