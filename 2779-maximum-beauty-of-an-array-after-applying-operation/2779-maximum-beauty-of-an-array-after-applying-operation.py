class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        # 정렬하고... 투포인터로 범위 잡으면 될 듯!
        # 1246
        nums.sort()

        res = 0

        left = 0
        for right in range(len(nums)):
            while nums[right] - nums[left] > 2 * k:
                left += 1

            res = max(res, right - left + 1)
        
        return res