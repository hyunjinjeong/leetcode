class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = []
        self.backtrack(0, [], target, candidates)
        return self.ans
    
    def backtrack(self, start, curr_array, target, candidates):
        if target < 0:
            return
        if target == 0:
            self.ans.append(curr_array[:])

        for i in range(start, len(candidates)):
            curr_array.append(candidates[i])
            self.backtrack(i, curr_array, target - candidates[i], candidates)
            curr_array.pop()