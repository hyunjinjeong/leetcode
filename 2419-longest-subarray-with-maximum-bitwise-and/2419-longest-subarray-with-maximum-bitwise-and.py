class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # 뭔 소리여..
        max_num = max(nums)

        res = 0
        curr = 0
        for num in nums:
            if num == max_num:
                curr += 1
            else:
                curr = 0
            res = max(res, curr)
        return res