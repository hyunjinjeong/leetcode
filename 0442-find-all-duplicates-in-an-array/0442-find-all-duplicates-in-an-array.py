class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        N = len(nums)

        # Flip (num - 1)th index
        # If the value has been already fliped, that means the num is duplicated

        res = []
        for i in range(N):
            num = abs(nums[i])

            if nums[num - 1] < 0:
                res.append(num)
            else:
                nums[num - 1] *= -1
        
        return res