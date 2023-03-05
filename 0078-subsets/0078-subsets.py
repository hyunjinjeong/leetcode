class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def dfs(start, curr):
            if start >= len(nums):
                return
            
            if curr not in ans:
                ans.append(curr)
            
            for i in range(start+1, len(nums)):
                dfs(i, curr + [nums[i]])
                dfs(i, curr)
        
        dfs(-1, [])
        return ans