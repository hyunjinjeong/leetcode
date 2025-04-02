class Solution:
    def check(self, nums: List[int]) -> bool:
        # nums + nums 해서 non decreasing 길이가 len(nums)가 되면 될 듯?
        N = len(nums)
        nums = nums + nums

        # 2 1 3 4 2 1 3 4
        
        streak = 0
        prev = 0
        for num in nums:
            streak = streak + 1 if num >= prev else 1
            if streak == N:
                return True
            prev = num
        return False