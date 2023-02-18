class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(current, visited):
            if len(current) == len(nums):
                answer.append(current)
                return
            
            for i in range(len(nums)):
                if i in visited:
                    continue
                
                visited.add(i)
                backtrack(current+[nums[i]], visited)
                visited.remove(i)
        
        answer = []
        backtrack([], set())
        return answer