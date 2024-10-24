class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        # 값 차이가 적은 순서대로 pair를 만들면 되려나?
        # 아니 binary search구나.. ㄷㄷ
        nums.sort()

        def count_pairs(diff):
            i, count = 0, 0
            while i < len(nums) - 1:
                if nums[i + 1] - nums[i] <= diff:
                    count += 1
                    i += 1
                i += 1
            return count
        
        left, right = 0, nums[-1] - nums[0]
        while left < right:
            mid = (left + right) // 2

            if count_pairs(mid) >= p:
                right = mid
            else:
                left = mid + 1
        
        return left