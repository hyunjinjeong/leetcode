class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(start, current_subset, max_length):
            if len(current_subset) == max_length:
                answer.append(current_subset[:])
                return
            
            for i in range(start, len(nums)):
                current_subset.append(nums[i])
                backtrack(i+1, current_subset, max_length)
                current_subset.pop()
        
        answer = []    
        for max_length in range(len(nums) + 1):
            backtrack(0, [], max_length)
        
        return answer