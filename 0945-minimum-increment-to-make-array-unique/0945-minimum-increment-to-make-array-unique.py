class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        # 1 1 2 2 3 7
        # 1 2 2 2 3 7 / 1
        # 1 2 3 2 3 7 / 2
        # 1 2 3 4 3 7 / 4
        # 1 2 3 4 5 7 / 6

        # 1 1 3 3 3 7
        # 1 2 3 3 3 7 / 1
        # 1 2 3 4 3 3
        nums.sort()

        count = 0

        prev = nums[0]
        for i in range(1, len(nums)):
            if nums[i] <= prev:
                count += prev - nums[i] + 1
                nums[i] = prev + 1
            prev = nums[i]
        
        return count
