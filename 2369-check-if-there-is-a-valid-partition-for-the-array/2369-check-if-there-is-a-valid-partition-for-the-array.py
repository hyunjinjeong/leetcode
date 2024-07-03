class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        # 3가지 경우 중에 하나인지를 dp로 계속해서 찾으면 되지 않을까?
        # 우선 top down으로 해보자...
        N = len(nums)

        @cache
        def dp(i):
            if i > N - 2:
                return False
            if i == N - 2:
                return nums[i] == nums[i+1]
            if i == N - 3:
                return nums[i] == nums[i+1] - 1 and nums[i+1] == nums[i+2] - 1 or nums[i] == nums[i+1] and nums[i+1] == nums[i+2]
            
            # 1. 2개 같은거
            result = False
            if nums[i] == nums[i+1] - 1 and nums[i+1] == nums[i+2] - 1 or nums[i] == nums[i+1] and nums[i+1] == nums[i+2]:
                result = result or dp(i+3)
            if nums[i] == nums[i+1]:
                result = result or dp(i+2)
            
            return result
        
        return dp(0)