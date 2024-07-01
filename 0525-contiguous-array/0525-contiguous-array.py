class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        ans = 0

        curr_sum = 0
        index_map = {0: -1} # 초기화

        for i, num in enumerate(nums):
            if num == 1:
                curr_sum += 1
            else:
                curr_sum -= 1
            
            if curr_sum in index_map:
                ans = max(i - index_map[curr_sum], ans)
            else:
                index_map[curr_sum] = i
        
        return ans
            
