class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        self.backtrack(0, [], nums)
        return self.ans

    def backtrack(self, start, current_subset, nums):
        self.ans.append(current_subset[:])
            
        for i in range(start, len(nums)):
            current_subset.append(nums[i])
            self.backtrack(i+1, current_subset, nums)
            current_subset.pop()