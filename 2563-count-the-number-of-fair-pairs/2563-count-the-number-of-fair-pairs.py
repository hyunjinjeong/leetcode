class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        # sorting 이었다..! 제약조건 때문에 너무 배제했네
        # 그러면 index 조건은 어떻게 검사하지..?
        # 가 아니라 검사할 필요가 없구나. nums[i] + nums[j]나 nums[j] + nums[i]나 같음
        # 0 1 4 4 5 7
        def bisect_left(target, start):
            lo, hi = start + 1, len(nums)
            while lo < hi:
                mid = lo + (hi - lo) // 2
                if target <= nums[mid]:
                    hi = mid
                else:
                    lo = mid + 1
            return lo

        nums.sort()
        pair_count = 0

        for i in range(len(nums)):
            lower_bound = bisect_left(lower - nums[i], i)
            upper_bound = bisect_left(upper - nums[i] + 1, i)

            pair_count += upper_bound - lower_bound
        
        return pair_count
