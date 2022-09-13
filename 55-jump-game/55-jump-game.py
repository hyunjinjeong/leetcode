class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        # top-down DP로 잘 했었넹.. 근데 이전 계산을 계속 반복해서 lru_cache가 필요했음.
        @lru_cache(None)
        def rec(curr_index):
            # 빠져나갈 곳들.
            if curr_index > len(nums) - 1:
                return False
            if curr_index == len(nums) - 1:
                return True
            
            for jump_length in range(nums[curr_index], 0, -1):
                if rec(curr_index + jump_length):
                    return True
            
            return False
            
        return rec(0)