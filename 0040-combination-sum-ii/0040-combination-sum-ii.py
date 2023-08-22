class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # 중복 방지를 위해 sort
        candidates.sort()
        return self.backtrack(0, [], target, candidates, [])
    
    def backtrack(self, start, curr_array, target, candidates, ans):
        if target < 0:
            return ans
        if target == 0:
            ans.append(curr_array[:])

        for i in range(start, len(candidates)):
            # 중복 방지
            if i > start and candidates[i] == candidates[i-1]:
                continue

            curr_array.append(candidates[i])
            # 중복 방지용 i + 1
            self.backtrack(i + 1, curr_array, target - candidates[i], candidates, ans)
            curr_array.pop()
        
        return ans