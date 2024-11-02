class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        res = nums[k]

        curr_min = nums[k]
        left, right = k, k 
        while left > 0 or right < len(nums) - 1:
            left_num = nums[left - 1] if left > 0 else 0
            right_num = nums[right + 1] if right < len(nums) - 1 else 0

            if left_num > right_num:
                left -= 1
                curr_min = min(curr_min, left_num)
            else:
                right += 1
                curr_min = min(curr_min, right_num)
            
            res = max(res, curr_min * (right - left + 1))
        
        return res