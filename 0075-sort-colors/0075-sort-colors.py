class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # # two-pass는 카운터 만들어서 하면 될듯
        # counter = collections.Counter(nums)
        
        # i = 0
        # for num in range(3):
        #     for _ in range(counter[num]):
        #         nums[i] = num
        #         i += 1

        # 1-pass. 
        zero, one, two = 0, 0, len(nums) - 1
        
        while one <= two:
            if nums[one] == 0:
                nums[zero], nums[one] = nums[one], nums[zero]
                zero += 1
                one += 1
            elif nums[one] == 1:
                one += 1
            else: # nums[one] == 2
                nums[one], nums[two] = nums[two], nums[one]
                two -= 1