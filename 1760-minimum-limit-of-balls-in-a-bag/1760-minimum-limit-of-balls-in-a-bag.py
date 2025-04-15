class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        # operation 1번마다 bag이 1개씩 늘어남
        # 즉 최종 개수는 len(nums) + maxOperations 개
        # 이때 min은 binary search로 찾으면 됨
        # 7 17 -> 7 7 10 -> 7 7 5 5
        # 24. 흠 이 예시는 그렇게 안 되는데...
        # 17 -> 

        def can_contain_all_balls(max_balls_in_bag):
            total_ops = 0
            for num in nums:
                ops = (num - 1) // max_balls_in_bag
                total_ops += ops
                if total_ops > maxOperations:
                    return False
            return True

        total_bags = len(nums) + maxOperations
        total_balls = sum(nums)

        lo, hi = 1, total_balls
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if can_contain_all_balls(mid):
                hi = mid
            else:
                lo = mid + 1

        return lo
