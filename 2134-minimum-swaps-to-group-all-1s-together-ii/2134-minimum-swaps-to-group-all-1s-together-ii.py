class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        # circular를 고려하지 않으면 어떻게 풀지? fixed window로 sliding 하면 될 듯
        # circular는? 그냥 nums + nums 배열로 계산하면 된다
        N = len(nums)
            
        one_count = nums.count(1)
        res = one_count
        
        window_zero_count = 0
        left = 0
        for right in range(N * 2):
            if nums[right % N] == 0:
                window_zero_count += 1
            
            if right - left + 1 > one_count:
                if nums[left % N] == 0: # lower bound
                    window_zero_count -= 1
                
                res = min(res, window_zero_count)
                left += 1

        return res
