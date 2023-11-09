class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # two-pass는 카운터 만들어서 하면 될듯
        counter = collections.Counter(nums)
        
        i = 0
        for num in range(3):
            for _ in range(counter[num]):
                nums[i] = num
                i += 1