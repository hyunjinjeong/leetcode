class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        N = len(nums)

        # Flip (num - 1)th index
        # If the value has been already fliped, that means the num is duplicated

        # res = []
        # for i in range(N):
        #     num = abs(nums[i])

        #     if nums[num - 1] < 0:
        #         res.append(num)
        #     else:
        #         nums[num - 1] *= -1
        
        # return res

        # cycle sort도 되네
        for i in range(N):
            while i != nums[i] - 1 and nums[i] != nums[nums[i] - 1]:
                # nums[i], nums[nums[i] - 1] = nums[nums[i] - 1], nums[i]
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        
        res = []
        for i in range(N):
            if nums[i] != i + 1:
                res.append(nums[i])
        
        return res