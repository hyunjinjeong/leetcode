class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # 추가 공간이 필요 없었음
        total_sum = sum(nums)
        left_sum = 0

        for i, num in enumerate(nums):
            if left_sum == total_sum - left_sum - num:
                return i
            left_sum += num
        
        return -1