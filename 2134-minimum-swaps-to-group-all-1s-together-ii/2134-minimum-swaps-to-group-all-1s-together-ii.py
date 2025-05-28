class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        # circular를 고려하지 않으면 어떻게 풀지? fixed window로 sliding 하면 될 듯
        # circular는? 그냥 nums + nums 배열로 계산하면 된다
        one_count, zero_count = 0, 0
        for num in nums:
            if num == 1:
                one_count += 1
            else:
                zero_count += 1
            
        window_zero_count = 0
        for i in range(one_count):
            if nums[i] == 0:
                window_zero_count += 1
        
        res = window_zero_count
        for i in range(one_count, len(nums) * 2):
            if nums[(i - one_count) % len(nums)] == 0: # prev_left
                window_zero_count -= 1
            if nums[i % len(nums)] == 0:
                window_zero_count += 1
            
            res = min(res, window_zero_count)

        return res
