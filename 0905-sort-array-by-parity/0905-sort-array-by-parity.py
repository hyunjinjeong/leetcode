class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # two pointer로 스왑하면 될 듯?
        left, right = 0, 0
        while right < len(nums):
            if nums[right] % 2 == 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right += 1
            else:
                right += 1
        
        return nums