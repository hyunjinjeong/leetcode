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
        # nums.sort()

        # count = 0
        # for i in range(1, len(nums)):
        #     if nums[i] <= nums[i - 1]:
        #         count += nums[i - 1] - nums[i] + 1
        #         nums[i] = nums[i - 1] + 1
        
        # return count
        # 이런 것도 되네
        counter = collections.Counter(nums)

        count = 0
        for num in range(len(nums) + max(nums)):
            if counter[num] >= 2:
                extra = counter[num] - 1
                counter[num + 1] += extra
                count += extra

        return count
