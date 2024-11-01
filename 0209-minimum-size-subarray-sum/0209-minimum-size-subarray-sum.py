class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # two pointer로 풀 수 있지 않을까?
        curr_sum, curr_len = 0, 0
        res = len(nums) + 1

        left = 0
        for right in range(len(nums)):
            curr_sum += nums[right]
            curr_len += 1

            while curr_sum >= target:
                res = min(res, right - left + 1)
                curr_sum -= nums[left]
                left += 1

        return res if res <= len(nums) else 0
